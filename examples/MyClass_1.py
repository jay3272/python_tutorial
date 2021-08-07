#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 04:52:38 2017

@author: justinwu
"""

class MyClass:
    i=12345
    
print(MyClass.i)

class Complex:
    def __init__(self,realpart,imagepart):
        self.r=realpart
        self.i=imagepart
        
x=Complex(3.0,-4.5)
print(x.r,x.i)

