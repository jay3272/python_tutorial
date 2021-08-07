#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:30:34 2017

@author: justinwu
"""

tp6=tuple([66,22,3,46,6,65,7,83,19])
print(tp6)
list1=list(tp6)
list1.sort()
print(list1)
print('-----------')
tp8=tuple(list1)
tp9=tuple(list1)
print(tp8)
print(tp8==tp9)