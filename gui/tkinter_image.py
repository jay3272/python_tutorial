#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:05:10 2018

@author: justinwu
"""

from tkinter import *
#安裝pillow
from PIL import Image, ImageTk
class Window(Frame):
    def __init__(self, master=None):      
        Frame.__init__(self, master)                
        self.master = master
        self.init_window()
    def init_window(self):   
        self.master.title("人機界面GUI")
        #使用包裝管理將widget視窗放到主視窗容器內
        self.pack(fill=BOTH, expand=1)        
        menu = Menu(self.master)#建立選單實體
        self.master.config(menu=menu)        
        file = Menu(menu)#建立檔案物件
        #加入離開命令command到選單選項,當事件發生執行client_exit()函數
        file.add_command(label="Exit離開", command=self.client_exit)
        #將檔案加入到選單
        menu.add_cascade(label="File檔案", menu=file)        
        edit = Menu(menu)#建立檔案物件
        #加入顯示圖片命令command到選單選項,當事件發生執行showImg()函數
        edit.add_command(label="顯示圖片", command=self.showImg)
        #加入顯示圖片命令command到選單選項,當事件發生執行showText()函數
        edit.add_command(label="顯示文字", command=self.showText)
        #將檔案加入到選單
        menu.add_cascade(label="編輯Edit", menu=edit)
    def showImg(self):
        load = Image.open("python.png")
        render = ImageTk.PhotoImage(load)
        #標籤可以是圖片或文字
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    def showText(self):
        text = Label(self, text="Hi 小文您好啊!")
        text.pack()      
    def client_exit(self):
        exit()

root = Tk()
root.geometry("380x300")
app = Window(root)
root.mainloop()  