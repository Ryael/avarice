"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the game-loop and global variables.
"""

from position import Position
import world
from constant import START_TITLE, END_TITLE
from helper import p_t, get_str
from player import Player

action_move_n_list = ["go n", "go north", "move n", "move north", "n", "north"]
action_move_s_list = ["go s", "go south", "move s", "move south", "s", "south"]
action_move_w_list = ["go w", "go west", "move w", "move west", "w", "west"]
action_move_e_list = ["go e", "go east", "move e", "move east", "e", "east"]


def start_game():
    """
    Starts the game, called at the end of game.py.
    Prints the game title.
    Lets the user decide whether to play or not.
    If they decline, this is noted and the game ends.
    If they accept, they are asked to provide a name.
    The user is given a choice whether to view the intro,
    after which the game begins.
    """
    p_t(START_TITLE)
    # Lets the user decide if they want to play the game.
    p_t("Investigator, do you accept the task?")
    start_choice = get_str("(Y/N):\n")
    if start_choice.lower()[0] == "y":
        p_t("\nThis task isn't for the faint of heart,")
        p_t("but we appreciate your help nonetheless.")
        p_t("We're confident that you're the right person for this job.")
        # Instantiates the player and requests a name and assigns it to
        # a variable.
        player = Player(Position(2, 0))
        p_t("Forgive my memory, I've dealt with a number of associates")
        p_t("lately.\n")
        player.name = get_str("Could you please state your name again?\n")
        p_t(f"\nVery well, Inspector {player.name}. Let's begin.")
        # Lets the user decide if they want to view the intro scene.
        intro_choice = get_str("\nShall we move onto the briefing? (Y/N):\n")
        if intro_choice.lower()[0] == "y":
            p_t("\nPlay intro scene")
            p_t("This will describe the back story of the Investigator")
            p_t("Their motives, why they approached, who approached them")
            p_t("and ultimately what their goal is")
            p_t("This will lead directly to the start of the game.")
        elif intro_choice.lower()[0] == "n":
            p_t("\nWe'll get straight to it then...")
        else:
            print("\nPlease answer the question, yes or no will suffice.")

        while True:
            # Spawns the player in the starting room.
            current_room = world.room_at(player.pos)
            if player.moved:
                if current_room.visited:
                    p_t("\n" + current_room.desc + "\n")
                else:
                    p_t("\n" + current_room.intro + "\n")
                    current_room.visited = True
            # Assigns movement actions to the player.
            action_input = get_player_command()
            if action_input in action_move_n_list:
                player.move(world.directions["n"])
            if action_input in action_move_s_list:
                player.move(world.directions["s"])
            if action_input in action_move_w_list:
                player.move(world.directions["w"])
            if action_input in action_move_e_list:
                player.move(world.directions["e"])
    elif start_choice.lower()[0] == "n":
        p_t("\nPerhaps another person would be better suited.")
        p_t("\nFarewell, Investigator.")
        p_t(END_TITLE)
    else:
        print("Please answer the question, yes or no will suffice.")


def get_player_command():
    """
    Returns the player's action.
    """
    return input("Action: ")


start_game()
