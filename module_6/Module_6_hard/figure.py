import math


class Figure:
    sides_count = 0  # Атрибут класса

    def __init__(self, color, *sides):
                # проверяем на количество переданных сторон, если кол-во сторон не равно sides_count,
        if len(sides) != self.sides_count:
                # то создаем массив с единичными сторонами и в том кол-ве, которое требует фигура.
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self) -> list:
        return list(self.__color)

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
            return False
        return True

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return

    def __is_valid_sides(self, *sides: int) -> bool:
        for side in sides:
            if isinstance(side, int) and side > 0:
                if len(sides) == len(self.__sides):
                    return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return
        else:
            for side in new_sides:
                self.__sides = [side]
