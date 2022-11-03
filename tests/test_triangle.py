import pytest
import src


def test_create():
    c = src.Triangle(10, 10, 10)
    sq = src.Square(5)
    assert c.area == 43.30127018922193, 'Площадь треугольника вычислилась неправильно'
    assert sq.area == 25, 'Площадь квадрата вычислилась неправильно'
    assert c.add_area(sq) == 68.30127018922192, 'Площадь квадрата и треугольника не сложилась или сложилась неправильно'




