# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:55:51 2019

@author: Administrator
"""

import os
import re


def post_move(name,out=r"./new/"):
    f1 = open('./old/'+name,'r+',encoding='utf-8')
    title,end=os.path.splitext(name)
    
    if out+name in os.listdir(out):
        os.remove(out+name)
        
    f2 = open(out+name,'w+',encoding='utf-8')
    
    f3=open('dt.txt','r+',encoding='utf-8')
    dt_list=f3.readlines()
    f3.close()
    for i in range(len(dt_list)):
        if dt_list[i].find(title) != -1:
            date=dt_list[i+2].split(r' 阅读数')[0]
            break       
    try:    
        cats=re.split('[()]',title)[1]
    except:
        cats=None
    header='''---
title: {title}
tags: [R]
mathjax: false
copyright: true
date: {date}
categories: [R,{cats}]
sticky: false
---'''.format(title=title,date=date,cats=cats)
    
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

name='SQL手册.md'

for name in os.listdir('./old/'):
    print(name)
    post_move(name)

os.chdir('./new/')
for old in os.listdir():
    new=old.replace(' ','-').replace('手册','Notebook')
    os.rename(old, new)