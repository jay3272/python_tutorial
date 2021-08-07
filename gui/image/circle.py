#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:10:32 2018

@author: justinwu
"""

from PIL import Image
LOGO_F='python-02.png'
logoIm=Image.open(LOGO_F)
width,heigh=logoIm.size
print(width,heigh)
print(logoIm.filename)
print(logoIm.format)
print(logoIm.format_description)
print(logoIm.save('python-03.jpg'))