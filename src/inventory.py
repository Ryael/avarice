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
    items: list = field(default_factory=list)

    def add_item(self, item):
        """
        Adds an item to the dictionary
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes and returns an Item from Inventory
        """
        if isinstance(item, str):
            item = self.__find_item(item)
        self.items.remove(item)

        return item

    def get_item(self, item_name):
        """
        returns an Item from Inventory
        """
        return self.__find_item(item_name)

    def is_empty(self):
        """
        Checks if inventory is empty
        """
        return True if len(self.items) == 0 else False

    def __find_item(self, item_name):
        """
        Finds an Item in own inventory
        """
        found_item = None
        for item in self.items:
            if len(item.name) >= 6 and len(item_name) >= 6:
                if item.name.lower()[:6] == item_name.lower()[:6]:
                    found_item = item
                    break
            else:
                if item.name.lower() == item_name.lower():
                    found_item = item
                    break

        return found_item
