#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 06:39:38 2017

@author: justinwu
"""
fp=open('file.txt','w')
if fp !=None:
    print('檔案開啟成功')
fp.close()

fp=open('file.txt','w')
if fp !=None:
    fp.write("小白")
fp.close()

fp=open('file.txt','w')
if fp !=None:
    fp.write("宇哲")
fp.close()

