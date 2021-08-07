#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:48:36 2017

@author: justinwu
"""

class Dog:
	kind = 'small dog'
	def __init__(self,name):
		self.name = name
        
d =Dog('small dog')
e = Dog('very small dog')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)