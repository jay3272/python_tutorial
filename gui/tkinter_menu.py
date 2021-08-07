#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:49:32 2018

@author: justinwu
"""

from tkinter import *
#Frame類別是在tkinter模組中
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("人機界面GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="離開Exit", command=self.client_exit)
        menu.add_cascade(label="檔案File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="編輯Edit", menu=edit)
    def client_exit(self):
        exit()
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()  