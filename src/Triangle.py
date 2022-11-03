from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print("Треугольник существует")
        else:
            raise ValueError('Такой треугольник не получится создать')

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        halfperimeter = self.perimeter / 2
        return math.sqrt(
            halfperimeter * (halfperimeter - self.a) * (halfperimeter - self.b) * (halfperimeter - self.c))






