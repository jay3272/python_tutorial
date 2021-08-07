#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:22:01 2018

@author: justinwu
"""

def concat(*args, sep="/"):
    return sep.join(args)
 
print(concat("earth", "mars", "venus"))

    
print(concat("earth", "mars", "venus", sep="."))    

