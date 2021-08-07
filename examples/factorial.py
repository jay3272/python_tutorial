#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:25:09 2017

@author: justinwu
"""

def factorial(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(1))
print(factorial(2))
print(factorial(3))