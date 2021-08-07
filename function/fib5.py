#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:47:39 2018

@author: justinwu
"""

def fib(n):
    a,b =0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
    
fib(1000)
print(fib)
f=fib
print(f)
f(500)