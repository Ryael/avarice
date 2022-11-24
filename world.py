"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains all the world details, lore, and location of items.
"""


class Room:
    """
    The core class for a room within the world.
    """
    def __init__(self, x_coord, y_coord):
        """
        Creates an instance of a new room.
        Parameter xco: the x-coordinate of the room.
        Parameter yco: the y-coordinate of the room.
        """
        self.x_coord = x_coord
        self.y_coord = y_coord

    def intro_text(self):
        """
        Information to be displayed when the player moves into this tile.
        """
        raise NotImplementedError()


class Observatory(Room):
    """
    Class for the starting room.
    """
    def intro_text(self):
        return """
        Starting room, a tall tower with windows on the top.
        """


class Kitchen(Room):
    """
    Class for the kitchen.
    """
    def intro_text(self):
        return """
        The kitchen, where the residents eat. Or perhaps it'll be more correct
        to say this is where they once ate.
        """


class Gate(Room):
    """
    Class for the main gate and the game's end point.
    """
    def intro_text(self):
        return """
        The main gate. You never thought you'd see the light of day after that
        harrowing experience, yet here you are.
        """


class Foyer(Room):
    """
    Class for the foyer.
    """
    def intro_text(self):
        return """
        The foyer, one of the first rooms people see.
        """


class Lobby(Room):
    """
    Class for the main lobby, where the monster is first found.
    """
    def intro_text(self):
        return """
        The main lobby, the room that connects all of the building together.
        """


class Dorm(Room):
    """
    Class for the dormitory.
    """
    def intro_text(self):
        return """
        The dormitory, where residents come to turn in for the night.
        """


class Toilets1(Room):
    """
    Class for the first toilets.
    """
    def intro_text(self):
        return """
        The first of two available toilet rooms.
        """


class Security(Room):
    """
    Class for the security centre.
    """
    def intro_text(self):
        return """
        The security centre, where the guards reside and watch over CCTV
        footage.
        """


class Common(Room):
    """
    Class for the common room.
    """
    def intro_text(self):
        return """
        The common room, where people gathered during their free time. It's
        also now the monster's nest.
        """


class Lab(Room):
    """
    Class for the research lab.
    """
    def intro_text(self):
        return """
        The research lab, where the monster was first cultivated by scientists.
        """


class Green(Room):
    """
    Class for the greenhouse.
    """
    def intro_text(self):
        return """
        The greenhouse, where fruit, vegetables, and plants are grown.
        """


class Garden(Room):
    """
    Class for the garden.
    """
    def intro_text(self):
        return """
        The garden, an open-air location with tall fences with electric wire
        on top. Not to prevent anyone from getting in, but rather to prevent
        something from getting out.
        """


class Play(Room):
    """
    Class for the playroom.
    """
    def intro_text(self):
        return """
        The playroom, where the monster grew up, played the piano (badly),
        was introduced to other animals, and ultimately, went insane.
        """


class Contain(Room):
    """
    Class for the containment room.
    """
    def intro_text(self):
        return """
        The containment area. This is was put whenever it started acting out.
        It also doubled as its resting area.
        """


class Sanitate(Room):
    """
    Class for the sanitation room.
    """
    def intro_text(self):
        return """
        The sanitation room, where the monster was regularly cleaned in order
        to maintain its hygiene. It was also fed here.
        """


class Data(Room):
    """
    Class for the Data Storage room.
    """
    def intro_text(self):
        return """
        Data storage room, where all the CCTV records, experimentation logs and
        research logs, and other sensitive information is kept.
        """


class Main(Room):
    """
    Class for the mainframe room.
    """
    def intro_text(self):
        return """
        The mainframe room. This is what powers the entire facility and where
        all the important computers are located.
        """


class Testing(Room):
    """
    Class for the testing room.
    """
    def intro_text(self):
        return """
        The testing room. This is where the monster's abilities were tested,
        including its endurance and health. Needless to say, it wasn't its
        favourite room.
        """


class Preserve(Room):
    """
    Class for the preservation room.
    """
    def intro_text(self):
        return """
        The perservation room, this place was used to nurse the monster back
        to health after any dangerous encounters. Or to make additional
        adjustments to its already mechnical body.
        """


class Toilets2(Room):
    """
    Class for the second toilets.
    """
    def intro_text(self):
        return """
        The second of the two toilets available in the facility.
        """


# Grid of the map, where the above classes slot in.
world_map = [
    [None, None, Observatory(2, 0), Kitchen(3, 0), None, None],
    [Gate(0, 1), Foyer(1, 1), Lobby(2, 1), Dorm(3, 1), Toilets1(4, 1), None],
    [None, Security(1, 2), Common(2, 2), Lab(3, 2), Green(4, 2), Garden(5, 2)],
    [Play(0, 3), Contain(1, 3), Sanitate(2, 3), Data(3, 3), Main(4, 3), None],
    [Testing(0, 4), Preserve(1, 4), None, None, Toilets2(4, 4), None]
]


def room_at(x_coord, y_coord):
    """
    Locates the room at a given coordinate.
    """
    if x_coord < 0 or y_coord < 0:
        return None
    try:
        return world_map[y_coord][x_coord]
    except IndexError:
        return None
