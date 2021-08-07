#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:09:08 2018

@author: justinwu
"""

from PIL import Image,ImageColor
myIm=Image.new('RGBA',(100,100))
myIm.getpixel((0,0))
for i in range(100):
    for j in range(50):
        myIm.putpixel((i,j),(0,255,0))
        
for i in range(100):
    for j in range(50,100):
        myIm.putpixel((i,j),ImageColor.getcolor('red','RGBA'))
        
print(myIm.getpixel((0,0)))
print(myIm.getpixel((0,50)))
myIm.save('Pixel_a.png')