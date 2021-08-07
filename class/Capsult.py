class Dog:
    def __init__(self,name):
        self.__name=name
        self.__tricks=[]

    def add_trick(self,trick):
        self.__tricks.append(trick)

    def printTrick(self):
        print(self.__name+str(self.__tricks))

d=Dog("小黑")
e=Dog("小白")
d.add_trick("翻滾")
d.add_trick("獵犬追蹤能力")
e.add_trick("靜止")
e.add_trick("很忠誠")
d.printTrick()
e.printTrick()