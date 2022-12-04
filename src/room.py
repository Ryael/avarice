"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the Room class.
"""

from dataclasses import dataclass, field
from inventory import Inventory
from position import Position
from event import Event


@dataclass
class Room:
    """
    The core class for a room within the world.
    """
    pos: Position
    name: str
    intro: str
    desc: str
    inventory: Inventory = field(default_factory=Inventory)
    visited: bool = False
    events: list = field(default_factory=list)
