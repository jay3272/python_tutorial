#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:34:11 2017

@author: justinwu
"""

st1=set()
st2=set([1,2,3,4,5])
st3={'a','b','c','d','e'}
print(st3)
print('-------')
st3.add('f')
print(st3)
st3.remove('d')
print(st3)
print('---------')
print(st3.union(st2))
st5={'a','b','c','d','e'}
print(st3.intersection(st5))
print(st3.difference(st5))