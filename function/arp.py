#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:00:32 2018

@author: justinwu
"""

def parrot(voltage,state='僵硬',action='飛',type='挪威藍'):
    print("-- 這隻鸚鵡將不會", action, end=' ')
    print("假如你放", voltage, "伏特電壓.")
    print("-- 可愛的羽毛,", type)
    print("-- 這是", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000,action='vooooom')
parrot(action='voltage',voltage=1000000)
parrot('一百萬','失去生命','跳')
parrot('一千',state='死去而被葬掉')