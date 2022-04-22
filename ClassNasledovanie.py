import math


class Figure:
    a = 1

    def area(self):
        pass

    def printArea(self):
        print(self.area())


class Rectangle(Figure):  # класс-ребёнок; в скобках - родитель
    side1 = 0
    side2 = 0

    def __init__(self, side1=None, side2=None):
        if side1 is None and side2 is None:
            pass
        elif side2 is None and not side2 is None:
            self.side1 = side1
            self.side2 = side1
        else:
            self.side1 = side1
            self.side2 = side2

    def area(self):
        return self.side1 ** self.side2


class Square(Rectangle):  # класс-ребёнок; в скобках - родитель
    def __init__(self, side):
        super().__init__(side, side)

    def __add__(self, n):
        self.side1 += n
        self.side2 += n
        return self

    def __str__(self):
        return 'side length = ' + str(self.side1)


s1 = Square(5)
print(s1)
s1+=1
r1 = Rectangle(2, 3)
print('Rectangle area = ', r1.area())
print(s1)