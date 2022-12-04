"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Room class.
"""

from dataclasses import dataclass, field
from inventory import Inventory
from position import Position
from helper import build_str, build_nameplate


@dataclass
class Room:
    """
    The core class for a room within the world.
    """
    pos: Position
    name: str
    intro: list
    desc: list
    inventory: Inventory = field(default_factory=Inventory)
    visited: bool = False
    events: list = field(default_factory=list)

    def introduction(self):
        """
        Returns introduction as a single string.
        """
        return build_nameplate(self.name) + \
            build_str(self.intro) + \
            self.room_items()

    def description(self):
        """
        Returns description as a single string.
        """
        return build_nameplate(self.name) + \
            build_str(self.desc) + \
            self.room_items()

    def room_items(self):
        """
        Returns a string containing the names of items in the room
        """
        if not hasattr(self, "inventory"):
            return ""

        if self.inventory.is_empty():
            return ""

        items_str = "\nYou see "
        first_item = True
        for item in self.inventory.items:
            if not first_item:
                items_str += "and "
            if not item.name.lower()[-1] == "s":
                if item.name.lower()[0] in ["a", "e", "i", "o", "u"]:
                    items_str += "an "
                else:
                    items_str += "a "
            items_str += item.name.upper() + " "
            first_item = False

        return items_str + "\n"

    def remove_item(self, item):
        """
        Adds an item to the player's inventory.
        """
        self.inventory.remove_item(item)
