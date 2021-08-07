#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:24:42 2017

@author: justinwu
"""

def fibonaci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
    
print(fibonaci(1))
print(fibonaci(2))
print(fibonaci(3))
print(fibonaci(4))
print(fibonaci(5))
print(fibonaci(20))