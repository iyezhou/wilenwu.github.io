#!/usr/bin/python
# -*- coding: utf-8 -*- 
    
import os
import re
import hashlib
import pandas as pd

root='D:\\wilenwu.github.io\\'
os.chdir(root)

def clean_inline(line):    
    key_value=line.split(': ')
    if len(key_value)==1:
        key=line[:-1] if line.endswith(':') else line
        return key.strip(' '),None
    elif len(key_value)==2:
        key,value=key_value
        if re.search('\[.*\]',value) is not None:     
            value=re.sub('[\[\]]','',value)
            value=re.split(',',value)
            value=[i.strip(' ') for i in value if not i.isspace()]
        else:
            value=[value]
    
    value_is_list=['categories','tags']
    value=value if key.lower() in value_is_list or len(value)>1 else value[0]
        
    return key.strip(''),value    

def clean_span(line):
    key=line[0][:-1] if line[0].endswith(':') else line[0]
    if re.search('^(\s*-)',line[1]) is not None:       
        value=[re.sub('^(\s*-)\s','',i) for i in line[1:]]
        value=[i for i in value if not i.isspace()]
    else:
        value=dict([clean_inline(i) for i in line[1:]])
    
    return key.strip(' '),value
    
def clean(content,YAML=True):
    content=re.sub('#.*?(?=\n)','',content)  # 去除注释(\s可以匹配到\n)
    content=re.sub('#.*$','',content)  # 去除最后一行注释
    content=re.sub('(\s*\n)+','\n',content) # 删除行尾空白并合并
    spans=re.split('\n(?![\s-])',content) # 分块
    spans=[i for i in spans if re.sub('\s','',i)!='']
    
    def split_span(span):
        if re.search('\n\s*(?!-)',span) is not None:
            space=re.search('\n\s*',span).group()
            line=re.split(space,span)           
        else:
            line=span.splitlines()
        return line
    
    lines=[split_span(i) for i in spans]  
    content_dict={}
    for line in lines:   # line=lines[2]
        if len(line)==1:
            line=line[0]
            key,value=clean_inline(line)
        elif len(line)>1:
            key,value=clean_span(line)
            
        if YAML and key.lower()=='title':
            key='post_title'
        elif YAML and key.lower()=='id':
            key='ID'
        else:
            key=key.lower()
            
        content_dict[key]=value
        
    return content_dict


# post_info
def get_post_info(post_url,updateID=False):
    with open(post_url,'r',encoding='utf-8') as f:
        post=f.read()
    
    boundary='\s*-{3,}\s*\n'  
    pattern='{b}.*?{b}'.format(b=boundary)
    YAML=re.search(pattern,post,re.DOTALL).group()  # 匹配YAML
    front_matter=re.sub(boundary,'',YAML)    # 删除起始标记    
    
    yaml_dict=clean(front_matter) # content=front_matter
    ID=yaml_dict['date'].encode(encoding='UTF-8')
    yaml_dict['ID']=hashlib.md5(ID).hexdigest()
    
    if updateID:
        YAML=re.sub('^\n+','',YAML)
        YAML=re.sub('\n+$','\n',YAML)
        new_yaml=re.sub('ID: .*\n+','',YAML,flags=re.I)
        new_yaml=re.sub('\n','\nID: '+yaml_dict['ID']+'\n',new_yaml,count=1)
        new_post=re.sub(pattern,new_yaml,post,count=1,flags=re.DOTALL)
        
        with open(post_url,'w',encoding='utf-8') as f:
            f.write(new_post)
    
    return yaml_dict



# bookshelf
def get_post_url(info_series,website,permalink): 
    permalink=re.sub(':id(?=[/\.])',':ID',permalink.lower())
    permalink=re.sub(':title(?=[/\.])',':post_name',permalink)
    link_keys=[i for i in permalink.split('/') if i.startswith(':') and i!='']
    
    for key in link_keys:
        key=re.sub('\..*?$','',key)
        value=info_series[key[1:]]
        
        if key==':post_name':
            value=os.path.splitext(value)[0]
            value='/'.join([info_series['post_path'],value])
        elif type(value)==list:
            value='/'.join(value)

        permalink=permalink.replace(key,value)
    return '/'.join([website,permalink])

def maps_collect(book,website,permalink,post_info): 
    lines=book.splitlines()
    maps={}
    
    post_info['shelftitle']=post_info['post_title'].apply(lambda x:re.sub('.+手册.*--','',x).lower())
    post_info['post_title']=post_info['post_title'].apply(lambda x:re.sub('\s','-',x))    
    post_info['date']=pd.to_datetime(post_info['date'])
    post_info['year']=post_info['date'].dt.year
    post_info['month']=post_info['date'].dt.month
    post_info['day']=post_info['date'].dt.day
    post_info=post_info.astype(str)
    
    for line in lines:
        line=re.sub('^(\s*-\s\[[ x]\])','',line) # 去除复选框的影响
        title_id=re.search('\[.+?\]\[.+?\]',line)
        if title_id is not None:
            shelftitle,shelfID=re.findall('(?<=\[).+?(?=\])',title_id.group())
            info_series=post_info.loc[post_info['shelftitle']==shelftitle.lower()]
            if info_series.size==0:
                continue
            else:
                info_series=info_series.iloc[0]
            
            post_url=get_post_url(info_series,website,permalink)
            maps[shelfID]=post_url                                          
    return maps     

def bookshelf_update(book,maps):   
    lines=book.splitlines()
    newbook=[]    
    for line in lines:
        shelfID=re.search('(?<=^\[).+(?=\]: )',line)
        if shelfID is None or shelfID.group() not in maps.keys():
            newbook.append(line+'\n')
        else:          
            shelfID=shelfID.group()
            post_url=maps[shelfID]
            newline='[{0}]: {1}'.format(shelfID,post_url)
            newbook.append(newline+'\n')

    return newbook

#-------------------------------------更新 
with open('_config.yml','r',encoding='utf-8') as f:
    config=f.read()
config=clean(config,YAML=False)
#content=config

source_dir=config['source_dir']
website=config['url']
permalink=config['permalink']
#permalink=':year/:month/:day/:title/'

#更新 post_info
posts_dir=os.path.join(source_dir,'_posts').replace('\\','/')
post_info=[]
for url, dirs, files in os.walk(posts_dir,topdown=False):
    for post_name in files:      
        post_url=os.path.join(url,post_name)
        yaml_dict=get_post_info(post_url,updateID=False)
        yaml_dict['post_name']=post_name
        yaml_dict['post_path']=re.sub(posts_dir+'/','',url.replace('\\','/'))
        post_info.append(yaml_dict)

post_info=pd.DataFrame(post_info)
post_info.to_csv(os.path.join(root,'script','post_info'),sep='\t',encoding='utf-8')

# url='source/_posts/R'
# post_name='RNotebook(Import)--read-csv-xlsx-or-json.md'

# 更新bookshelf
os.chdir(os.path.join(source_dir,'bookshelf'))
books=os.listdir()

#path='PythonBookshelf.md'

for path in books:
    with open(path,'r',encoding='utf-8') as f:
        book=f.read()        
    maps=maps_collect(book,website,permalink,post_info)
    newbook=bookshelf_update(book,maps)
    with open(path,'w',encoding='utf-8') as f:
        f.writelines(newbook)
