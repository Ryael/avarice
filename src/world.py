"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains all the world and its generation.
"""

import yaml

with open("avarice_yaml/avarice_paths.yml", "r", encoding="utf-8") as file:
    paths = yaml.load(file, Loader=yaml.Loader)

with open("avarice_yaml/avarice_rooms.yml", "r", encoding="utf-8") as file:
    rooms = yaml.load(file, Loader=yaml.Loader)


def generate_world():
    """
    Generates the world map.
    """
    max_x = 0
    max_y = 0
    rooms_map = []

    for room in rooms:
        if room.pos.x > max_x:
            max_x = room.pos.x
        if room.pos.y > max_y:
            max_y = room.pos.y

    for row in range(max_y + 1):
        row = []

        num = 0
        while num < max_x + 1:
            row.append(None)
            num += 1

        rooms_map.append(row)

    for room in rooms:
        rooms_map[room.pos.y][room.pos.x] = room

    return rooms_map


def room_at(pos):
    """
    Locates the room at a given coordinate.
    """
    try:
        return world_map[pos.y][pos.x]
    except IndexError:
        return None


def path_at(pos, dest):
    """
    Locates the path between two given coordinates.
    """
    try:
        return find_path(pos, dest)
    except IndexError:
        return None


def find_path(pos, dest):
    """
    Checks if the path exists.
    """
    for path in paths:
        if path.exists(pos, dest):
            return path

    return None


world_map = generate_world()
