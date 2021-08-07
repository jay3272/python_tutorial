#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:39:39 2017

@author: justinwu
"""

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
fruits.count('apple')
fruits.index('banana')
fruits.index('banana',4)#Finding next banana starting a position 4

fruits.reverse()

print(fruits)

fruits.append('grape')

print(fruits)

fruits.sort()

print(fruits)

fruits.pop()
