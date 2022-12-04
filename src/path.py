"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Path class.
"""

from dataclasses import dataclass
from position import Position
from helper import build_str


@dataclass
class Path:
    """
    The core path for the map within the world.
    """
    desc: list
    room1: Position
    room2: Position
    locked: bool = False
    blocked: bool = False

    def exists(self, pos, dest):
        """
        Checks if room coordinated exist in this path
        """
        if (pos in [self.room1, self.room2] and
           dest in [self.room1, self.room2]):
            return True

        return False

    def description(self):
        """
        Returns description as a single string.
        """
        return build_str(self.desc)
