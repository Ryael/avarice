"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the room generation logic.
"""


class Path:
    """
    The core path for the map within the world.
    """
    def __init__(self, desc):
        """
         Creates an instance of a new path.
         Parameter desc = description of the path.
        """
        self.desc = desc
