#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:26:07 2018

@author: justinwu
"""

def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")
     
     
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

print(parrot(**d))     