#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:40:39 2017

@author: justinwu
"""
tel={'Justin':'0920909872','Ivy':'0922876895'}
tel['Johny']='0920885356'
print(tel)
print(tel['Johny'])
del tel['Johny']
tel['Mary']='0922865255'
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('Ivy' in tel)
print('Johny' in tel)