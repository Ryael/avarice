"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the game-loop and global variables.
"""

import time
from position import Position
import world
from player import Player

action_move_n_list = ["go n", "go north", "move n", "move north", "n", "north"]
action_move_s_list = ["go s", "go south", "move s", "move south", "s", "south"]
action_move_w_list = ["go w", "go west", "move w", "move west", "w", "west"]
action_move_e_list = ["go e", "go east", "move e", "move east", "e", "east"]


def p_t(text):
    """
    Print a line of text.
    The function name is abbreviated to permit for longer text strings.
    For clarity: "p_t" stands for print text.
    """
    time.sleep(0.75)
    print(text)


def get_str(question):
    """Returns a non-empty string, input by the user.
    Runs a while loop, using the "question" parameter to seek user input.
    If an empty string is given (i.e. the user just presses ENTER),
    or if the user inputs only spaces,
    the loop will print an error message and request input again.
    Also removes extra whitespace from strings.
    Adapted from a function by Siobhán Mooney:
    https://github.com/Estelindis/double-agent
    """
    while True:
        input_str = input(f"{question}\n")
        input_str = " ".join(input_str.split())
        if input_str.strip() == "":
            input_str = ""
        if not input_str:
            time.sleep(0.75)
            print("Please input something rather than nothing.")
        else:
            return input_str


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
    p_t("""\033[38;2;150;95;143m
█████╗ ██╗   ██╗ █████╗ ██████╗ ██╗ ██████╗███████╗
██╔══██╗██║   ██║██╔══██╗██╔══██╗██║██╔════╝██╔════╝
███████║██║   ██║███████║██████╔╝██║██║     █████╗
██╔══██║╚██╗ ██╔╝██╔══██║██╔══██╗██║██║     ██╔══╝
██║  ██║ ╚████╔╝ ██║  ██║██║  ██║██║╚██████╗███████╗
╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝ \033[0m\n""")
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
        p_t("""\033[38;2;150;95;143m
████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔
            \033[0m""")
        p_t("Perhaps another person would be better suited.")
        p_t("\nFarewell, Investigator.\n")
    else:
        print("Please answer the question, yes or no will suffice.")


def get_player_command():
    """
    Returns the player's action.
    """
    return input("Action: ")


start_game()
