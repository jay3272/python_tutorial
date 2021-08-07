class Dog:
    def __init__(self,name):
        self.__name=name
        self.__tricks=[] #建立串列

    def add_trick(self,trick):
        self.__tricks.append(trick)
    def printTrick(self):
        print(self.__name+str(self.__tricks))

d = Dog('小黑')
e = Dog('小白')

d.add_trick('翻滾')
e.add_trick('靜止')
d.printTrick()
e.printTrick()
