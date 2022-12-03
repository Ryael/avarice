"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Path class.
"""

from dataclasses import dataclass
from room import Room


@dataclass
class Path:
    """
    The core path for the map within the world.
    """
    desc: str
    room1: Room
    room2: Room
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
