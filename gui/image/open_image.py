#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:33:37 2018

@author: justinwu
"""

from PIL import Image
LOGO_F= 'python-02.png'
logoIm = Image.open(LOGO_F)
width,heigh=logoIm.size
print(width,heigh)
print(logoIm.filename)
print(logoIm.format)
print(logoIm.format_description)
print(logoIm.save('python-02.jpg'))

