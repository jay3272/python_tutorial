#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:36:56 2017

@author: justinwu
"""

import matplotlib.pyplot as pt
month1=[1,2,3,4,5,6,10,12]
month2=[1,3,4,5,6,7,11,12]
sale1 =[20000,40000,60000,80000,100000,120000,140000,160000]
sale2 =[10000,20000,30000,150000,120000,80000,60000,210000]
pt.plot(month1,sale1,lw=2,label='Ivy Lin')
pt.plot(month2,sale2,lw=2,label='Johny Wu')
pt.xlabel('month')
pt.ylabel('dollars')
pt.legend()
pt.title('matplotlib example')
pt.show()