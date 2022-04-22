import math


class Coordinate:
    x = 1
    y = 5

    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __init__(self):
        pass
    def distance(self, x, y):
        print(math.sqrt(x ** 2 + y ** 2))

    @staticmethod
    def distance(x, y, z):
        print(math.sqrt(x ** 2 + y ** 2 + z ** 2))


ivan = Coordinate(5, 6)
andrey = Coordinate()
ivan.a = 2
ivan.func(2, 5)
