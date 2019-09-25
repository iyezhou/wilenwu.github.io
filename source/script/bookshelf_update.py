#!/usr/bin/python
# -*- coding: utf-8 -*- 
    
import os
import re
import hashlib
import pandas as pd

root='D:\\wilenwu.github.io\\'
os.chdir(root)

website='https://wilenwu.github.io'
permalink='posts/:title.html'
source_dir='source'
posts_path=source_dir+'\\_posts\\'

def clean(line):
    if len(line)==1:
        line=line[0]
        key_value=line.split(': ')
        if len(key_value)==1:
            key=line[:-1] if line.endswith(':') else line
            return key.strip(' '),None
        elif len(key_value)==2:
            line=re.sub('(?<=: )\[|\]$','',line)
            line=re.split(': |,',line)
            key=line[0]
            value=[i.strip(' ') for i in line[1:] if not i.isspace()]
            value=value[0] if len(value)==1 else value
            return key.strip(''),value
    elif len(line)>1:
        key=line[0][:-1] if line[0].endswith(':') else line[0]
        value=[re.sub('^-\s','',i) for i in line[1:]]
        value=[i.strip(' ') for i in value if not i.isspace()]
        value=value[0] if len(value)==1 else value
        return key.strip(' '),value    

def get_post_info(post_url,updateID=False):
    with open(post_url,'r',encoding='utf-8') as f:
        post=f.read()
        
    pattern='{b}.*?{b}'.format(b='\s*-{3,}\s*\n')
    YAML=re.search(pattern,post,re.DOTALL).group()  # 匹配YAML
    front_matter=re.sub('\s*-{3,}\s*\n','',YAML)  # 起始标记
    front_matter=re.sub('#.*?(?=\n)','',front_matter)  # 去除注释
    front_matter=re.sub('(\s*\n\s*)+','\n',front_matter) # 并去除行首行尾空白并合并
    front_matter=re.split('\n(?!\s|-)',front_matter) # 分块
    
    lines=[i.splitlines() for i in front_matter]
    
    yaml_dict={}
    for line in lines:
        key,value=clean(line)
        key=key.upper() if key.lower()=='id' else key
        yaml_dict[key]=value
    
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

post_info=[]
for url, dirs, files in os.walk(posts_path, topdown=False):
    for post_name in files:         
        print(post_name)
        post_url=os.path.join(url,post_name)  
        yaml_dict=get_post_info(post_url,updateID=False)
        post_info.append(yaml_dict)

post_info=pd.DataFrame(post_info).set_index('ID')
