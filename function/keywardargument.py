#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:13:21 2018

@author: justinwu
"""

def parrot(voltage, state='僵硬', action='飛', type='挪威藍'):
    print("-- 這隻鸚鵡將不會", action, end=' ')
    print("假如你放", voltage, "伏特電壓.")
    print("-- 可愛的羽毛,", type)
    print("-- 這是", state, "!")
    
    
parrot(1000)                                          # 位置1引數
parrot(voltage=1000)                                  # 1個關鍵引數
parrot(voltage=1000000, action='VOOOOOM')             # 2個關鍵引數
parrot(action='飛飛', voltage=1000000)             # 2個關鍵引數
parrot('一百萬', '失去生命', '跳')         # 3個位置引數
parrot('一千', state='死去而被葬掉')  # 1個位置引數,1個關鍵引數


#parrot()                     # 需要的引數沒有放入
#parrot(voltage=5.0, 'dead')  # 關鍵引數後需要有關鍵引數
#parrot(110, voltage=220)     # 一樣的引數帶入兩次
#parrot(actor='John Cleese')  # 沒有關鍵引數叫actor