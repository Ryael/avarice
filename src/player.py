"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the logic dictating everything concerning the player.
"""


from world import path_at


class Player:
    """
    The core class for the player character within the world.
    """
    def __init__(self, pos):
        """
        Creates an instance of the player character and assigns x,y coordinates
        to them to represent their position within the world.
        """
        self.pos = pos
        self.moved = True
        self.inventory = {}

    def move(self, d_pos):
        """
        The move method is called using named parameteres, these parameteres
        are from math and represent changes in x and y values. This method
        accepts a change in the x and/or y directions. It moves the player
        if the path exists, and doesn't if the path doesn't exist. It also
        checks if the path is either blocked or locked.
        """
        path = valid_move(self, d_pos)

        if path is not None:
            if path.blocked or path.locked:
                print(path.desc)
            else:
                self.pos += d_pos
                self.moved = True
                return

        self.moved = False
        print("""
        You find yourself unable to move in that direction.
        """)

    def add_item(self, item_id, item):
        """
        Adds an item to the player's inventory.
        """
        self.inventory[item_id] = item


def valid_move(player, d_pos):
    """
    Checks if the path being moved into exists.
    """
    dest = player.pos + d_pos
    path = path_at(player.pos, dest)

    if path is not None:
        return path

    return None
