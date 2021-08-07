#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:11:29 2018

@author: justinwu
"""

from tkinter import *

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title("人機界面GUI")
        self.pack(fill=BOTH,expand=1)
        quitButton=Button(self,text="Quit離開")
        quitButton.place(x=100,y=100)
        
root=Tk()
root.geometry("200x200")
app=Window(root)
root.mainloop()