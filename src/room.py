"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Room class.
"""


class Room:
    """
    The core class for a room within the world.
    """
    def __init__(self, pos, name, intro, desc):
        """
        Creates an instance of a new room.
        Parameter x_pos: the x-coordinate of the room.
        Parameter y_pos: the y-coordinate of the room.
        """
        self.pos = pos
        self.name = name
        self.visited = False
        self.intro = intro
        self.desc = desc
        self.items = {}
