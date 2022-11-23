"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains all the world details, lore, and location of items.

"""


class Room:
    """
    The core class for a room within the world.
    """
    def __init__(self, xco, yco):
        """Creates an instance of a new room.
        Parameter xco: the x-coordinate of the room.
        Parameter yco: the y-coordinate of the room.
        """
        self.xco = xco
        self.yco = yco

    def intro_text(self):
        """
        Information to be displayed when the player moves into this tile.
        """
        raise NotImplementedError()
