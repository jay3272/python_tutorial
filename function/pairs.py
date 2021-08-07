#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:29:37 2018

@author: justinwu
"""

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair: pair[1])

print(pairs)

