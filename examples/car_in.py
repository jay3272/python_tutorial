#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vehicle:
    def __init__(self,name,engine):
        self.__name=name
        self.__engine=engine
        
    def getName(self):
        return self.__name
    def getEngine(self):
        return self.__engine
    
class Car(Vehicle):
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)
        self.__electric=electric      
       
    def getEngine(self):
        return ("超級")
    
    def getAuto(self):
        print("自動駕駛車")
        
myCar=Car("特斯拉","磁電Engine","電力")
myCar.getAuto()
print(myCar.getEngine())
print(Vehicle.getEngine())
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    