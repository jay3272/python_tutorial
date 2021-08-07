#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:37:53 2018

@author: justinwu
"""

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


