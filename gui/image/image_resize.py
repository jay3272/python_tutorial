#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:20:12 2018

@author: justinwu
"""

from PIL import Image
LOGO_F= 'python-02.png'
logoIm = Image.open(LOGO_F)
print(logoIm.size)
width,heigh=logoIm.size
logoIm_1=logoIm.resize((int(width/4),int(heigh/4)))
print(logoIm_1.size)
logoIm_1.save('new_half_fixed.png')
logoIm_2=logoIm.resize((width+2000,heigh))
print(logoIm_2.size)
logoIm_2.save('new_width.png')
logoIm.rotate(180).save('new_rotate_180.png')
logoIm.transpose(Image.FLIP_TOP_BOTTOM).save('new_hori_flip.png')