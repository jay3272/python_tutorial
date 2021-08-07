#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:56:58 2018

@author: justinwu
"""

#! python3
#將本目錄的所有圖片都加上PNG.png圖片


import os
from PIL import Image
S_SIZE = 1800
LOGO_F= 'PNG.png'
logoIm = Image.open(LOGO_F)
logoWidth, logoHeight = logoIm.size
#新增image目錄
os.makedirs('image_a', exist_ok=True)
#搜尋目前目錄的所有檔案＃選取所有png檔和jpg檔或檔名為LOGO_F
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_F:
        continue 
    im = Image.open(filename)#打開LOGO_F檔案
    width, height = im.size
    #檢查影像大小是否要被修正
    if width > S_SIZE and height > S_SIZE:
        if width > height:
            height = int((S_SIZE / width) * height)
            width = S_SIZE
        else:
            width = int((S_SIZE / height) * width)
            height = S_SIZE
        # 更新圖片大小
        print('更新圖片大小 %s...' % (filename))
        im = im.resize((width, height))
    # 將圖片加入LOGO_F.
    print('將圖片加入LOGO_F %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    # 儲存圖片.
    im.save(os.path.join('image_a', filename))
