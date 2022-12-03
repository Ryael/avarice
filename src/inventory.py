"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the logic dictating everything concerning the Invetories.
"""

from dataclasses import dataclass, field


@dataclass
class Inventory:
    """
    Contains items in a dictionary
    """
    items: dict = field(default_factory=dict)

    def add_item(self, identifier, item):
        """
        Adds an item to the dictionary
        """
        self.items[identifier] = item

    def remove_item(self, identifier):
        """
        Removes and returns an Item from Inventory
        """
        item = self.items[identifier]
        self.items[identifier] = None

        return item

    def get_item(self, identifier):
        """
        returns an Item from Inventory
        """
        return self.items[identifier]
