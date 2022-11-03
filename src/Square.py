from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        self.a = a

    @property
    def perimeter(self):
        return 2 * (self.a + self.a)

    @property
    def area(self):
        return self.a * self.a
