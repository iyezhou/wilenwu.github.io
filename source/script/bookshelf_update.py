#!/usr/bin/python
# -*- coding: utf-8 -*- 
    
import os
import re
import pandas as pd

site_path='D:\\wilenwu.github.io\\'
os.chdir(site_path)

def get_info_inline(text):
    lines=text.splitlines()
    for line in lines:
        line=line.split('#')[0].rstrip(' ')
    if line.find(': ')>0:
        key,value=line.split(': ')
        value=value.strip(' ').replace('\n','')
        
        re.sub()
        re.split()

with open('_config.yml','r',encoding='utf-8') as f:
    site_config=f.read()
    
for line in site_config:
    n=line.find('#')
    if n>0:
        line=line[:n]
    line=line.strip(' ')
    if line.find(': ')>0:
        key,value=line.split(': ')
        value=value.strip(' ').replace('\n','')
    
    if key.lower()=='url':
        website=value
    elif key.lower()=='permalink':
        permalink=value
    elif key.lower()=='source_dir': 
        source_dir=value

posts_path=site_path+'source\\_posts'
post_info=pd.DataFrame()
for urls, dirs, files in os.walk(posts_path, topdown=False):
    for post_name in files:
        post_url=os.path.join(urls,post_name)
        post_info.loc[post_name,'post_url']=post_url
        
        with open(post_url,'r',encoding='utf-8') as f:
            post=f.readlines()
            
        front_matter=0
        for line in post:
            line=line.strip(' ')
            if front_matter==1 and line.find(': ')>0:
                key,value=line.split(': ')
                value=value.strip(' ').replace('\n','')
                post_info.loc[post_name,key]=value
            elif front_matter==2:
                break
            if line.startswith('---'):
                front_matter+=1 

        

post_info.to_csv('post_info.csv',sep='\t',encoding='utf-8')
    
