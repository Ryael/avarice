"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the items present in the game as well as their
containers.
"""

from dataclasses import dataclass, field
from helper import build_str


@dataclass
class Item:
    """
    The base class for all items within the game.
    """
    name: str
    desc: list = field(default_factory=list)
    room_desc: list = field(default_factory=list)
    takeable: bool = False

    def description(self):
        """
        Returns description as a single string.
        """
        return build_str(self.desc)

    def room_description(self):
        """
        Returns description as a single string.
        """
        return build_str(self.room_desc)

    def take(self, _player_inventory):
        """
        Lets the user take a takeable item.
        """
        if self.takeable:
            return self

        return None


@dataclass
class Container(Item):
    """
    A container for another item.
    """
    contained_item: Item = field(default_factory=Item)
    required_item: str = None
    required_item_desc: list = field(default_factory=list)

    def take(self, player_inventory):
        """
        Lets the player take the item in the container.
        """
        if self.required_item is None:
            return self.contained_item

        if player_inventory.get_item(self.required_item) is not None:
            return self.contained_item

        print("\n" + self.required_item_description() + "\n")
        return None

    def required_item_description(self):
        """
        Returns a description of the required item.
        """
        return build_str(self.required_item_desc)
