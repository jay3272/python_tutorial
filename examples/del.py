#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:16:28 2017

@author: justinwu
"""

class Complex:
    def __init__(self,realpart,imagepart):
        self.r=realpart
        self.i=imagepart
        
    def __del__(self):
        print('物件被解構刪除了')
        
x=Complex(3.0,-4.5)
print(x.r,x.i)
x=None