#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:28:01 2018

@author: justinwu
"""

def make_incrementor(n):
     return lambda x: x + n
 
f = make_incrementor(42)
print(f(0))
print(f(1))   

 