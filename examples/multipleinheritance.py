# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine

    def getName(self):
        return self.__name
    
    def getEngine(self):
        return self.__engine

    def setEngine(self,engine):
        self.__engine = engine

class Electric:
    def __init_(self,PowerElectric):
        self.__PowerElectric = PowerElectric
        
    def getPower(self):
        return self.__PowerElectric
    
    def setPower(self,PowerElectric):
        self.__PowerElectric = PowerElectric
        
    
    
class Car(Vehicle,Electric):
    def __init__(self,name,engine,PowerElectric,auto):
        super().__init__(name,engine)
        self.setPower(PowerElectric)
        self.__Auto = auto

    def getCarName(self):
        print("名子:"+self.getName())
        print("引擎:"+self.getEngine())
        print("電動車:"+self.getPower())  
        
    def getAuto(self):
        return self.__Auto
    

myCar = Car("特斯拉","磁電Engine","電力","自動駕駛車")
myCar.getCarName()
myCar.getAuto()