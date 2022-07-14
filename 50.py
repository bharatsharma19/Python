from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 4
        self.breadth = 6

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())


