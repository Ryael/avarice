"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the actions present in the game.
"""

from position import Position

directions = {
    "n": Position(0, -1),
    "e": Position(1, 0),
    "s": Position(0, 1),
    "w": Position(-1, 0)
}

move_north = ["north", "n"]
move_east = ["east", "e"]
move_south = ["south", "s"]
move_west = ["west", "w"]
move_actions = ["go", "move"] + move_north + move_east + move_south + move_west
examine_actions = ["examine", "exam", "ex"]
recall_actions = ["recall", "r"]


# Return {type: 'MOVE', dir: 'S'}
def get_player_command():
    """
    Returns the player's action.
    """
    #
    command = input("\033[38;2;191;97;72mYour action: \033[0m").split(" ", 1)
    action = command[0]
    argument = None
    if len(command) > 1:
        argument = command[1].replace("  ", " ")

    # Move type action.
    if action in move_actions:
        if action in move_north or argument in move_north:
            return {"action_type": 'MOVE', "direction": 'n'}
        if action in move_east or argument in move_east:
            return {"action_type": 'MOVE', "direction": 'e'}
        if action in move_south or argument in move_south:
            return {"action_type": 'MOVE', "direction": 's'}
        if action in move_west or argument in move_west:
            return {"action_type": 'MOVE', "direction": 'w'}

    # Examine action.
    if action in examine_actions:
        return {"action_type": 'EXAMINE', "item": argument}

    # Recall action.
    if action in recall_actions:
        return {"action_type": 'RECALL'}

    return None
