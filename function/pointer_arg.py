#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:13:00 2018

@author: justinwu
"""

def concat(*args,sep='/'):
    return sep.join(args)

print(concat("earth","mars",'venus',"林小寶","詹麗雲"))

print(concat("earth","mars",'venus',"林小寶","詹麗雲",sep='.'))