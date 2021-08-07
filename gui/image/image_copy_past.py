#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:01:23 2018

@author: justinwu
"""

from PIL import Image
LOGO_F= 'python-02.png'
logoIm = Image.open(LOGO_F)
myCopy = logoIm.copy()
width,heigh=logoIm.size
print(width,heigh)
logoIm=logoIm.crop((6000,2000,7000,3000))
myCopy.paste(logoIm,(100,100))
myCopy.paste(logoIm,(2000,2000))
myCopy.save('new_fixed.png')


