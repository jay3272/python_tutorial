#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:16:01 2018

@author: justinwu
"""
#從tkinter人機界面套件輸入所有模組
from tkinter import *

class Window(Frame):
    #初始化視窗
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
#建立最上層視窗        
root = Tk()
#建立視窗實體
app = Window(root)
#顯示視窗和執行主體迴圈
root.mainloop()       

 