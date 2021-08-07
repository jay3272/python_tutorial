#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:01:44 2018

@author: justinwu
"""

from PIL import Image,ImageColor

myIm=Image.new('RGBA',(100,100))
myIm.getpixel((0,0))
for i in range(100):
    for j in range(50):
        myIm.putpixel((i,j),(255,255,255))
        
for i in range(100):
    for j in range(50,100):
        myIm.putpixel((i,j),\
           ImageColor.getcolor('red','RGBA'))
        
print(myIm.getpixel((0,0)))
print(myIm.getpixel((0,50)))
myIm.save('Pixel_1.png')

myIm=Image.new('RGBA',(100,100))
myIm.getpixel((0,0))
for i in range(100):
    for j in range(50):
        myIm.putpixel((i,j),(255,255,255))
        
for i in range(100):
    for j in range(50,100):
        myIm.putpixel((i,j),\
            ImageColor.getcolor('green','RGBA'))
        
print(myIm.getpixel((0,0)))
print(myIm.getpixel((0,50)))
myIm.save('Pixel_2.png')

myIm=Image.new('RGBA',(100,100))
myIm.getpixel((0,0))
for i in range(100):
    for j in range(50):
        myIm.putpixel((i,j),(255,255,255))
        
for i in range(100):
    for j in range(50,100):
        myIm.putpixel((i,j),\
            ImageColor.getcolor('blue','RGBA'))
        
print(myIm.getpixel((0,0)))
print(myIm.getpixel((0,50)))
myIm.save('Pixel_3.png')
