#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:03:46 2018

@author: justinwu
"""

def cheeseshop(kind ,*arguments,**keywords):
    print("--Do you have any",kind,"?")
    print("--I'm sorry,we're all out of",kind)
    for arg in arguments:
        print(arg)
        
    for kw in keywords:
        print(kw,":",keywords[kw])
        
cheeseshop("Limburger","AA","BB","CC","DD","EE",shopkeeper="林小寶",client="詹麗雲",sketch="江小文")        