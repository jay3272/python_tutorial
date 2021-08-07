#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:34:31 2018

@author: justinwu
"""

import os 
from PIL import Image
S_SIZE=1800
LOGO_F='PNG.png'
logoIm=Image.open(LOGO_F)
logoWidth,logoHeight=logoIm.size
os.makedirs('image_b',exist_ok=True)
for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg')) or filename==LOGO_F: 
        continue
    im=Image.open(filename)
    width,height=im.size
    if width>S_SIZE and height>S_SIZE:
        if width>height:
            height=int((S_SIZE/width)*height)
            width=S_SIZE
        else:
            width=int((S_SIZE/height)*width)
            height=S_SIZE
        print('更新圖片大小%s...'%(filename))
        im=im.resize((width,height))
    print('將圖片加入LOGO_F%s...'%(filename))
    im.paste(logoIm,(width-logoWidth,height-logoHeight),logoIm)
    im.save(os.path.join('image_b',filename))
    
    
    
    
    
    
    