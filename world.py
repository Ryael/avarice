"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains all the world details, lore, and location of items.
"""

from path import Path

paths = [
    Path("Locked", [0, 1], [1, 1]),  # Main Gate & Foyer
    Path("Locked", [1, 2], [1, 3]),  # Security Centre & Containment
    Path("Blocked", [0, 3], [0, 4]),  # Play Room & Testing
    Path("Blocked", [3, 2], [3, 3]),  # Research Lab & Data Storage
    Path("Blocked", [3, 2], [4, 2]),  # Research Lab & Greenhouse
    Path("Blocked", [1, 2], [2, 2]),  # Security Centre & Common Room
    Path("Open", [2, 0], [2, 1]),  # Observatory & Main Lobby
    Path("Open", [2, 1], [3, 1]),  # Main Loby & Dormitory
    Path("Open", [3, 1], [3, 0]),  # Dormitory & Kitchen
    Path("Open", [3, 1], [4, 1]),  # Dormitory & Toilets(1)
    Path("Open", [2, 1], [1, 1]),  # Main Lobby & Foyer
    Path("Open", [1, 1], [1, 2]),  # Foyer & Security Centre
    Path("Open", [2, 1], [2, 2]),  # Main Lobby & Common Room
    Path("Open", [2, 2], [3, 2]),  # Common Room & Research Lab
    Path("Open", [2, 2], [2, 3]),  # Common Room & Sanitation
    Path("Open", [2, 3], [1, 3]),  # Sanitation & Containment
    Path("Open", [1, 3], [0, 3]),  # Containment & Play Room
    Path("Open", [1, 3], [1, 4]),  # Containment & Preservation
    Path("Open", [2, 3], [3, 3]),  # Sanitation & Data Storage
    Path("Open", [3, 3], [4, 3]),  # Data Storage & Mainframe
    Path("Open", [4, 3], [4, 4]),  # Mainframe & Toilets(2)
    Path("Open", [4, 3], [4, 2]),  # Mainframe & Greenhouse
    Path("Open", [4, 2], [5, 2])  # Greenhouse & Garden
]


class Room:
    """
    The core class for a room within the world.
    """
    def __init__(self, x_pos, y_pos):
        """
        Creates an instance of a new room.
        Parameter x_pos: the x-coordinate of the room.
        Parameter y_pos: the y-coordinate of the room.
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

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
        Starting room, a tall tower with windows on the top.\n

        You hear faint noises coming from the south. Perhaps it's worth
        investigating...
        """


class Kitchen(Room):
    """
    Class for the kitchen.
    """
    def intro_text(self):
        return """
        The kitchen, where the residents eat. Or perhaps it'll be more correct
        to say this is where they once ate.\n

        Not much else here, just a dead end.
        """


class Gate(Room):
    """
    Class for the main gate and the game's end point.
    """
    def intro_text(self):
        return """
        The main gate. Once sealed shut, now open.\n

        You never thought you'd see the light of day after that
        harrowing experience, yet here you are.
        """


class Foyer(Room):
    """
    Class for the foyer.
    """
    def intro_text(self):
        return """
        The foyer, one of the first rooms people see.\n

        To the east you see the main entrance for the facility. It looks sealed
        shut and you realise that you won't be able to leave without find a
        key. It's never that simple, is it... You hear a faint beeping sound
        coming from the south.
        """


class Lobby(Room):
    """
    Class for the main lobby, where the monster is first found.
    """
    def intro_text(self):
        return """
        The main lobby, the room that connects all of the building together.\n

        The noise you heard coming from the south is now much louder. It seems
        eerily... mechanical. Maybe avoiding that path for now would be for the
        best. After all, you still do have two other paths you could explore.
        """


class Dorm(Room):
    """
    Class for the dormitory.
    """
    def intro_text(self):
        return """
        The dormitory, where residents come to turn in for the night.\n

        To the north you see a sign reading "Kitchen" and to the east
        you see a sign reading "Toilets".
        """


class Toilets1(Room):
    """
    Class for the first toilets.
    """
    def intro_text(self):
        return """
        The first of two available toilet rooms.\n

        There's nothing else of interest here.
        """


class Security(Room):
    """
    Class for the security centre.
    """
    def intro_text(self):
        return """
        The security centre, where the guards reside and watch over CCTV
        footage.\n

        You see a huge metallic two-part door to the south, but much
        like the entrance is also sealed shut.
        """


class Common(Room):
    """
    Class for the common room.
    """
    def intro_text(self):
        return """
        The common room, where people gathered during their free time. It's
        also now the monster's nest.\n

        A horrible smell overwhelms as you look up to see a sign reading
        "Sanitation". You're suddenly overwhelmed with dread.
        """


class Lab(Room):
    """
    Class for the research lab.
    """
    def intro_text(self):
        return """
        The research lab, where the monster was first cultivated by scientists.
        \n

        A horrible smell overwhelms as you look up to see a sign reading
        "Sanitation". You're suddenly overwhelmed with dread.
        """


class Green(Room):
    """
    Class for the greenhouse.
    """
    def intro_text(self):
        return """
        The greenhouse, where fruit, vegetables, and plants are grown.\n

        Directions from the Greenhouse.
        """


class Garden(Room):
    """
    Class for the garden.
    """
    def intro_text(self):
        return """
        The garden, an open-air location with tall fences with electric wire
        on top. Not to prevent anyone from getting in, but rather to prevent
        something from getting out.\n

        Directions from the Garden.
        """


class Play(Room):
    """
    Class for the playroom.
    """
    def intro_text(self):
        return """
        The playroom, where the monster grew up, played the piano (badly),
        was introduced to other animals, and ultimately, went insane.\n

        Directions from Play Room.
        """


class Contain(Room):
    """
    Class for the containment room.
    """
    def intro_text(self):
        return """
        The containment area. This is was put whenever it started acting out.
        It also doubled as its resting area.\n

        Directions from Containment.
        """


class Sanitate(Room):
    """
    Class for the sanitation room.
    """
    def intro_text(self):
        return """
        The sanitation room, where the monster was regularly cleaned in order
        to maintain its hygiene. It was also fed here.\n

        Directions from Sanitation.
        """


class Data(Room):
    """
    Class for the Data Storage room.
    """
    def intro_text(self):
        return """
        Data storage room, where all the CCTV records, experimentation logs and
        research logs, and other sensitive information is kept.\n

        Directions from Data Storage.
        """


class Main(Room):
    """
    Class for the mainframe room.
    """
    def intro_text(self):
        return """
        The mainframe room. This is what powers the entire facility and where
        all the important computers are located.\n

        Directions from Mainframe room.
        """


class Testing(Room):
    """
    Class for the testing room.
    """
    def intro_text(self):
        return """
        The testing room. This is where the monster's abilities were tested,
        including its endurance and health. Needless to say, it wasn't its
        favourite room.\n

        Directions from Testing.
        """


class Preserve(Room):
    """
    Class for the preservation room.
    """
    def intro_text(self):
        return """
        The perservation room, this place was used to nurse the monster back
        to health after any dangerous encounters. Or to make additional
        adjustments to its already mechnical body.\n

        Directions from Preservation.
        """


class Toilets2(Room):
    """
    Class for the second toilets.
    """
    def intro_text(self):
        return """
        The second of the two toilets available in the facility.\n

        Directions from the second existing toilets.
        """


# Grid of the map, where the above classes slot in.
world_map = [
    [None, None, Observatory(2, 0), Kitchen(3, 0), None, None],
    [Gate(0, 1), Foyer(1, 1), Lobby(2, 1), Dorm(3, 1), Toilets1(4, 1), None],
    [None, Security(1, 2), Common(2, 2), Lab(3, 2), Green(4, 2), Garden(5, 2)],
    [Play(0, 3), Contain(1, 3), Sanitate(2, 3), Data(3, 3), Main(4, 3), None],
    [Testing(0, 4), Preserve(1, 4), None, None, Toilets2(4, 4), None]
]


def room_at(x_pos, y_pos):
    """
    Locates the room at a given coordinate.
    """
    if x_pos < 0 or y_pos < 0:
        return None
    try:
        return world_map[y_pos][x_pos]
    except IndexError:
        return None


def path_at(x_pos, y_pos, x_dest, y_dest):
    """
    Locates the path between two given coordinates.
    """
    try:
        return find_path([[x_pos, y_pos], [x_dest, y_dest]])
    except IndexError:
        return None


def find_path(path_coords):
    """
    Checks if the path exists.
    """
    for path in paths:
        if path_coords == path.between:
            return path
        if (path_coords[0] == path.between[1] and
                path_coords[1] == path.between[0]):
            return path

        return None
