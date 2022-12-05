"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Position class.
"""


from dataclasses import dataclass


@dataclass
class Position:
    """
    Core class for position management.
    """
    x: int
    y: int

    def __add__(self, pos):
        new_x = self.x + pos.x
        new_y = self.y + pos.y

        return Position(new_x, new_y)

    def __iadd__(self, pos):
        self.x += pos.x
        self.y += pos.y

        return self

    def __cmp__(self, pos):
        if self.x == pos.x and self.y == pos.y:
            return True

        return False
