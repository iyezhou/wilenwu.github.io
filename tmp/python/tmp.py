# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:55:51 2019

@author: Administrator
"""

import os
import re


def post_move(name,out=r"./new/"):
    f1 = open(name,'r+',encoding='utf-8')
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
        
    cats=re.split('[()]',title)[1]
    header='''
---
title: {title}
tags: [python]
mathjax: false
copyright: true
date: {date}
categories: [python,{cats}]
sticky: false
---
'''.format(title=title,date=date,cats=cats)
    
    f2.write(header+'\n')
    
    more=True
    for line in f1.readlines():
        line=line.replace('\ufeff','')
        if line.find('[toc]')!=-1 or line.find('利用Python进行数据分析')!=-1:
            continue
        elif line.find(r'# ')!=-1 and more:
            more=False
            f2.write('<!-- more -->\n\n')
            f2.write(line)
        else:
            f2.write(line)
    link='''
    参考链接：
    [《利用Python进行数据分析·第2版》](https://www.jianshu.com/p/04d180d90a3f)
    '''
    f2.write('\n\n\n')
    f1.close()
    f2.close()





for name in os.listdir():
    title,end=os.path.splitext(name)
    if end==r'.md':
        post_move(name,out='./new/')