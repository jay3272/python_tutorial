class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine

    def getName(sef):
        return self.__name
    
    def getEngine(self):
        return self.__engine

    def setEngine(self,engine):
        return self.__engine = engine

    
class Car(Vehicle):
    def __init__(self,name,engine,target):
        super().__init__(name,engine)
        self.__target = target

    def getCarName(self):
        print(""+self.getName())
        print(""+self.getEngine())
