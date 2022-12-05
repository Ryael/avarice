"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the logic dictating everything concerning the player.
"""

from dataclasses import dataclass, field
from world import path_at
from inventory import Inventory
from position import Position


@dataclass
class Player:
    """
    The core class for the player character within the world.
    """
    pos: Position
    inventory: Inventory = field(default_factory=Inventory)
    moved = True

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
            if path.blocked:
                print(path.description())
            elif path.locked:
                if self.inventory.get_item(path.required_item) is not None:
                    path.locked = False
                    print("\nYou unlock the path and proceed onward.")
                    self.pos += d_pos
                    self.moved = True
                    return
                else:
                    print(path.description())
            else:
                self.pos += d_pos
                self.moved = True
                return

        self.moved = False
        print("\nYou find yourself unable to move in that direction.\n")

    def add_item(self, item):
        """
        Adds an item to the player's inventory.
        """
        self.inventory.add_item(item)

    def examine(self, current_room, item_name):
        """
        Examines an Item in the room or inventory.
        """
        self.moved = False
        if item_name is None:
            print("\nWhat did you want to examine?")
            return

        current_room_item = current_room.inventory.get_item(item_name)
        player_inventory_item = self.inventory.get_item(item_name)

        if current_room_item is not None:
            print("\n" + current_room_item.room_description())
            taken_item = current_room_item.take(self.inventory)
            if taken_item is not None:
                self.add_item(taken_item)
                current_room.remove_item(current_room_item)
                print("You obtain the " + taken_item.name.upper() + ".\n")
            return
        if player_inventory_item is not None:
            print("\n" + player_inventory_item.description())
            return

        print("\nYou don't see that here.\n")


def valid_move(player, d_pos):
    """
    Checks if the path being moved into exists.
    """
    dest = player.pos + d_pos
    path = path_at(player.pos, dest)

    if path is not None:
        return path

    return None
