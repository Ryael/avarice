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
        return build_nameplate(self.name) + build_str(self.intro)

    def description(self):
        """
        Returns description as a single string.
        """
        return build_nameplate(self.name) + build_str(self.desc)

    def remove_item(self, item):
        """
        Adds an item to the player's inventory.
        """
        self.inventory.remove_item(item)
