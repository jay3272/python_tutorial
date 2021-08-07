#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:58:06 2017

@author: justinwu
"""

while True:
    try:
        x=int(input("Please enter a number:"))
        break
    except ValueError:
        print("input error")