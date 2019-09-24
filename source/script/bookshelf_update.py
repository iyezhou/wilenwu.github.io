#!/usr/bin/python
# -*- coding: utf-8 -*- 
    
import os
import re
import pandas as pd

site_path='D:\\wilenwu.github.io\\'
os.chdir(site_path)

def get_info_span(str_span):
    str_span=re.split('\n(?! |-|#)',str_span)
    cleaned={}
    
    def get_info_inline(str_inline):
        key_value=str_inline.split(': ')
        if len(key_value)==1:
            key=key_value[0]
            value=None
        else:
            key,value=key_value
            value=re.sub('[\[\]]','',value.strip(' ')).split(',')
            
        key=key.strip(' ')     
        return key,value
        
    for line in str_span:
        line=re.sub(' *#[.\u4e00-\u9fa5]* *(?=\n)','',line).splitlines()
        line=[i for i in line if i.replace(' ','')!='']
                    
        if len(line)==1 and line[0].find(': ')>0:
            key,value=get_info_inline(line[0])
            cleaned[key]=value
        elif len(line)>1 and line[1].lstrip(' ')[0]=='-':
            key=line[0].replace(': ','').strip(' ')
            value=[i.replace('-','').strip(' ') for i in line[1:]]
            cleaned[key]=value
        elif len(line)>1 and line[1].startswith(' '):
            key=line[0].replace(': ','').strip(' ')
            value={}
            for string in line[1:]:
                k,v=get_info_inline(string)
                value[k]=v
            cleaned[key]=value
    return cleaned          


website='https://wilenwu.github.io'
permalink='posts/:title.html'
source_dir='source'

posts_path=source_dir+'\\_posts\\'
post_info=pd.DataFrame()

for urls, dirs, files in os.walk(posts_path, topdown=False):
    for post_name in files:
        post_url=os.path.join(urls,post_name)
        post_info.loc[post_name,'post_url']=post_url
        
        with open(post_url,'r',encoding='utf-8') as f:
            post=f.readlines()
        front_matter=re.search('^( *-{3,})\s*\n.*?(\s*-{3,}) *\n',post,re.DOTALL).group()
        front_matter=re.sub('^( *-{3,})\s*\n|( *-{3,})\s*\n','',front_matter)  
        
        get_info_span(front_matter) 


post_info.to_csv('post_info.csv',sep='\t',encoding='utf-8')
    
