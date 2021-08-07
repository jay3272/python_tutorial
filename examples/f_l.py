#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:14:19 2017

@author: justinwu
"""

def myreturn(x,y):
    return x*y

i3=2
i5=5
i8=myreturn(i3,i5)
print(i8)

def myreturn(a,x=2,y=3):
    return a*x*y
i3=2
i5=5
i8=myreturn(8,i3,i5)
print(i8)
i8=myreturn(8)
print(i8)