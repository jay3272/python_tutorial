#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:06:58 2017

@author: justinwu
"""
import sys
try:
    f=open('mysql.pyo')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print("OSError:(0)",format(err))
except ValueError:
    print("Could not convert data to integer.")
except:
    print("Unexpected error:",sys.exc_info()[0])