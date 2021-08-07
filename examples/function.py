#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:58:23 2017

@author: justinwu
"""
i = 10
def f():
    print(i)

i = 42
f()

def addf(x,y):
    print(x+y)
    
i1=23
i2=12
addf(23,12)

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