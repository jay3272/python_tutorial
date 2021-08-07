import Shape
import math
class Circle(Shape.point):
    def __init__(self,radius,x=0,y=0):
        super().__init(x,y)
        self.radius=radius

    def area(self):
        return math.pi*(self.radius**2)

    def __eq__(self,other):
        return "Circle({0.radius!r},{0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return repr(self)