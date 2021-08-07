#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:54:58 2018

@author: justinwu
"""
from tkinter import *
from PIL import Image,ImageTk


class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title("人機界面GUI")
        
        self.pack(fill=BOTH,expand=1)
        menu=Menu(self.master)
        self.master.config(menu=menu)
        file=Menu(menu)
        file.add_command(label='Exit離開',command=self.client_exit)
        menu.add_cascade(label='File檔案',menu=file)
        edit=Menu(menu)
        edit.add_command(label='顯示圖片',command=self.showImg)
        edit.add_command(label='顯示文字',command=self.showText)
        menu.add_cascade(label='編輯Edit',menu=edit)
        
    def showImg(self):
        load=Image.open('python.png')
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=50)
        
    def showText(self):
        text=Label(self,text='Hi小文您好啊')
        text.pack()
        
    def client_exit(self):
        exit()
        
root=Tk()
root.geometry('380x300')
app=Window(root)
root.mainloop()        
        
        
        
        
        
        
        
        
        
        