"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the items present in the game as well as the inventory.
"""

from dataclasses import dataclass
from helper import build_str


@dataclass
class Item:
    """
    The base class for all items within the game.
    """
    name: str
    desc: list

    def description(self):
        """
        Returns description as a single string.
        """
        return build_str(self.desc)
