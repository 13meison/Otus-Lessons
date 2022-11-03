from src.Figure import Figure


class Circle(Figure):
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def perimeter(self):
        return self.diameter * 3.14

    @property
    def area(self):
        return self.diameter ** 2 / 4 * 3.14


c = Circle(10)
print(c.area)
