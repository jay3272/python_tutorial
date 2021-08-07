#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:46:34 2018

@author: justinwu
"""

def parrot(voltage, state='僵硬', action='飛'):
    print("-- 這隻鸚鵡將不會", action, end=' ')
    print("假如你放", voltage, "伏特電壓.")
    print("-- 這是", state, "!")
    

d={"voltage":1000000,"state":'失去生命',"action":'VOOOOOM'}    
parrot(**d) # 位置1引數

