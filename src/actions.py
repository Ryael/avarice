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

action_move_n_list = ["go n", "go north", "move n", "move north", "n", "north"]
action_move_s_list = ["go s", "go south", "move s", "move south", "s", "south"]
action_move_w_list = ["go w", "go west", "move w", "move west", "w", "west"]
action_move_e_list = ["go e", "go east", "move e", "move east", "e", "east"]


# Return {type: 'MOVE', dir: 'S'}
def get_player_command():
    """
    Returns the player's action.
    """
    # Add validations here
    command = input("\033[38;2;191;97;72mYour action: \033[0m")

    # Move type
    if command in action_move_n_list:
        return {"action_type": 'MOVE', "direction": 'n'}
    if command in action_move_s_list:
        return {"action_type": 'MOVE', "direction": 's'}
    if command in action_move_w_list:
        return {"action_type": 'MOVE', "direction": 'w'}
    if command in action_move_e_list:
        return {"action_type": 'MOVE', "direction": 'e'}

    # Examine
    if command in ["examine", "exam"]:
        return {"action_type": 'EXAMINE'}
