#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:50:34 2018

@author: justinwu
"""

from tkinter import *
class MouseKeyEvent:
    def __init__(self,window):
        window.title("滑鼠按鍵事件")
        mycanvas=Canvas(window,bg='white',width=300,height=300)
        mycanvas.pack()
        mycanvas.bind('<Key>',self.KeyEvent)
        mycanvas.focus_set()
        mycanvas.bind('<Button-1>',self.MouseEvent)
        window.mainloop()
        
    def KeyEvent(self,event):
        print('鍵盤按鍵符號',event.keysym)
        print('鍵盤按鍵碼',event.keycode)
        print('鍵盤輸入字元',event.char)
        
    def MouseEvent(self,event):
        print('滑鼠座標',event.x,event.y)
        print('滑鼠在視窗的位置',event.x_root,event.y_root)
        print('按下哪一個滑鼠按鈕',event.num)

mywindow=Tk()
MouseKeyEvent(mywindow)        


