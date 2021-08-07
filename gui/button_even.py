#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:50:21 2018

@author: justinwu
"""

from tkinter import *  
#從tkinter人機界面套件輸入所有模組
class Window(Frame):
    ##初始化視窗
    def __init__(self, master=None):      
        # Frame類別初始化,並將主視窗帶入. 
        Frame.__init__(self, master)   
        #參考master的tk視窗                 
        self.master = master
        #執行init_window()
        self.init_window()
    #init_window（）建立
    def init_window(self):
        #改變我們主視窗的名稱   
        self.master.title("GUI")
        #使用包裝管理將widget視窗放到主視窗容器內
        self.pack(fill=BOTH, expand=1)
        #建立按鈕實體
        quitButton = Button(self, text="Exit",command=self.client_exit)
        #放置按鈕到視窗主體中
        quitButton.place(x=0, y=0)
    def client_exit(self):
        exit()
root = Tk()#建立主視窗
root.geometry("400x300")#設定視窗大小400*300
app = Window(root)#建立視窗實體
root.mainloop()  #主迴圈mainloop 