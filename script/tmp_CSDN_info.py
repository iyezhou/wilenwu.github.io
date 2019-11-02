# -*- coding: utf-8 -*-

import os
import re
import hashlib

def hash(string):
    ID=string.encode(encoding='UTF-8')
    return hashlib.md5(ID).hexdigest()

def post_move(name,out=r"./new/"):
    f1 = open('./old/'+name,'r+',encoding='utf-8')
    title,end=os.path.splitext(name)
    
    if out+name in os.listdir(out):
        os.remove(out+name)
        
    f2 = open(out+name,'w+',encoding='utf-8')
    
    f3=open('dt.txt','r+',encoding='utf-8')
    dt_list=f3.read().splitlines()
    f3.close()
    for i in range(len(dt_list)):
        if dt_list[i].find(title) != -1:
            date=dt_list[i+2].split(r' 阅读数')[0]
            break       
    try:    
        tag=re.split('[()]',title)[1]
    except:
        tag=None
    header='''---
ID: {ID}
title: {title}
tags: [Math,{tag}]
mathjax: true
copyright: true
date: {date}
categories: [Foundations Math]
sticky: false
---'''.format(ID=hash(date),title=re.sub('\(.+\)','',title),date=date,tag=tag)
    
    f2.write(header+'\n')
    
    more=True
    for line in f1.readlines():
        line=line.replace('\ufeff','')
        if line.find('[toc]')!=-1 or line.find('利用Python进行数据分析')!=-1:
            continue
        elif line.find(r'# ')!=-1 and more:
            more=False
            f2.write('<!-- more -->\n')
            f2.write(line)
        else:
            f2.write(line)

    f2.write('\n\n\n')
    f1.close()
    f2.close()

name='初等数学公式(Elementary mathematical formula).md'

for name in os.listdir('./old/'):
    print(name)
    post_move(name)

os.chdir('./new/')
for old in os.listdir():
    title,end=os.path.splitext(old)
    new=title.replace(' ','-').replace('手册','Notebook')
    new=re.split('[()]',new)[1]
    os.rename(old, new+end)