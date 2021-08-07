#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:49:52 2018

@author: justinwu
"""

def fib2(n):  # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result
 
f100=fib2(100)
print(f100)    