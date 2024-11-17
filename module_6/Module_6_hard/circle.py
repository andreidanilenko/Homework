from figure import Figure
import math

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2