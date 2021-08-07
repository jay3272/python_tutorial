#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:49:28 2018

@author: justinwu
"""

from PIL import Image
LOGO_F= 'python-02.png'
logoIm = Image.open(LOGO_F)
width,heigh=logoIm.size
print(width,heigh)
logoIm=logoIm.crop((5500,2000,6500,3000))
print(logoIm.save('mycrop.png'))
width,heigh=logoIm.size
print(width,heigh)

