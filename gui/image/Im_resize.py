#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:28:58 2018

@author: justinwu
"""

from PIL import Image
LOGO_F='python-02.png'
logoIm=Image.open(LOGO_F)
width,heigh=logoIm.size
print(width,heigh)
logoIm_1=logoIm.resize((int(width/4),int(heigh/4)))
print(logoIm_1.size)
logoIm_1.save('new_half_fixed3.png')
logoIm_2=logoIm.resize((width+2000,heigh))
print(logoIm_2.size)
logoIm_2.save('new_width3.png')
logoIm.rotate(180).save('new_rotate3_180.png')
logoIm.transpose(Image.FLIP_TOP_BOTTOM).save('new_horizontal_flip.png')