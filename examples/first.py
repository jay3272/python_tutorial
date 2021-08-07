# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:08:28 2017

@author: justinwu
"""
import numpy
import scipy
dir(scipy)
dir(numpy)
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]

[[row[i] for row in matrix] for i in range(4)]

transposed = []

for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
