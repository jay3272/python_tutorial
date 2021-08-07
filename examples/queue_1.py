#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:39:53 2017

@author: justinwu
"""

from collections import deque
queue = deque(['阿呆','Eric','John','Michael','小寶','小文'])
print(queue)
queue.append('Terry')
print(queue)
queue.append('Graham')
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

