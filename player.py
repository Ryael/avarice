"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the logic dictating everything concerning the player.
"""


class Player:
    """
    The core class for the player character within the world.
    """
    def __init__(self):
        """
        Creates an instance of the player character and assigns x,y coordinates
        to them to represent their position within the world.
        """
        self.x_coord = 1
        self.y_coord = 2
