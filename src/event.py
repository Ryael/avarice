"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains all the events.
"""

from dataclasses import dataclass
from helper import build_str
from item import Item


@dataclass
class Event:
    """
    Contains an event within the game.
    """
    action: str
    desc: list
    item: Item = None

    def description(self):
        """
        Returns description as a single string.
        """
        return build_str(self.desc)
