import Shape
p=Shape.Point(20,30)
c=Shape.Circle(5,20,30)
print(c.area())
print(repr(p))#repr()函數
print(repr(c))#會對給定的物件呼叫__repr__()特殊方法
print(c.radius)