#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:20:03 2018

@author: justinwu
"""

from PIL import Image
Logo_F='python-02.png'
logoIm=Image.open(LOGO_F)
mycopy=logoIm.copy()
width,heigh=logoIm.size
print(width,heigh)
logoIm=logoIm.crop((5500,2000,6500,3000))
mycopy.paste(logoIm,(100,100))
mycopy.paste(logoIm,(2000,2000))
print(mycopy.save('new_fixed_a.png'))
