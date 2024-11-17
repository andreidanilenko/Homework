from module_6.Module_6_hard.figure import Figure
import math


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        a, b, c = self.get_sides
        p = (a + b + c) / 2  # полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))  # формула  Герона