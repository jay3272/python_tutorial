#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 06:46:03 2017

@author: justinwu
"""

fp=open('file.txt','r')
if fp !=None:
    str=fp.read()
    print(str)
fp.close()

fp=open('file.txt','r')
if fp !=None:
    strList=fp.readlines()
    print(strList)
fp.close()