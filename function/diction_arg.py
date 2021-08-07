#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:17:23 2018

@author: justinwu
"""

def parrot(voltage,state='僵硬',action='飛'):
        print("--這隻鸚鵡將不會",action,end=' ')
        print("假如你放",voltage,"伏特電壓.")
        print("--這是",state,"!")
        
d={"voltage":10000000,"state":"失去生命","action":"VoooooM"}

parrot(**d)