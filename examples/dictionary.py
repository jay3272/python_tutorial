#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:40:10 2017

@author: justinwu
"""

import pandas as pd

SalarysDic ={"John":'50000',
        "Mary":'20000',
        "Ivy":'90000',
        "Steve":'35000',
        "David":'85000'
        }
myDic = pd.Series(SalarysDic,index=SalarysDic.keys())
print(myDic[0])
print(myDic['Ivy'])
print(myDic[[0,1,3]])
print(myDic[['John','Ivy','David']])
