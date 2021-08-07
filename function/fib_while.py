#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:47:22 2018

@author: justinwu
"""

def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
     
fib(2000)
print(fib)
f = fib
print(f)
f(100)    