#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:56:18 2018

@author: justinwu
"""

def f(a,L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))