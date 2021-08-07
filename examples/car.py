#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:38:54 2017

@author: justinwu
"""

class Vehicle:
    def __init__(self,name,engine):
        self.__name=name
        self.__engine=engine
        
    def getName(self):
        return self.__name
    
    def getEngine(self):
        return self.__engine

    def setEngine(self,engine):
        self.__engine = engine
        
class Car(Vehicle):
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)
        self.__electric=electric
        
    def getCarName(self):
        print("名子",self.getName())
        print("引擎:"+self.getEngine())
        print("電動車"+self.__electric)
        
    def getAuto(self):
        print("自動駕駛車")
        
        
myCar = Car("特斯拉","磁電Engine","電力")
myCar.getCarName()
myCar.getAuto()