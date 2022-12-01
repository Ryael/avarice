"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Path class.
"""


class Path:
    """
    The core path for the map within the world.
    """
    def __init__(self, room1, room2, desc, locked=False, blocked=False):
        """
         Creates an instance of a new path.
         Parameter desc = description of the path.
         Parameters room1 & room2 = path between two rooms.
         Parameters lock and block: locked and blocked paths.
        """
        self.desc = desc
        self.room1 = room1
        self.room2 = room2
        self.locked = locked
        self.blocked = blocked

    def exists(self, pos, dest):
        """
        Checks if room coordinated exist in this path
        """
        if (pos in [self.room1, self.room2] and
           dest in [self.room1, self.room2]):
            return True

        return False
