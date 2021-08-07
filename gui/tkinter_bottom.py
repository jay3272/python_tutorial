#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:32:17 2018

@author: justinwu
"""

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
    #建立初始化視窗
    def init_window(self):
        #改變主視窗的名稱     
        self.master.title("人機界面GUI")
        #使用包裝管理將widget視窗放到主視窗容器內
        self.pack(fill=BOTH, expand=1)
        # 建立按鈕實體
        quitButton = Button(self, text="Quit離開")
        # 將按鈕實體放到(100,100)座標位置
        quitButton.place(x=100, y=100)
root = Tk()
#視窗大小設定
root.geometry("200x200")
app = Window(root)
root.mainloop()  