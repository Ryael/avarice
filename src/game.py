"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the game-loop.
"""

import actions
import world
from constant import START_POSITION, START_TITLE, END_TITLE
from helper import p_t, get_str


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
    start_choice = get_str("Investigator, do you accept the task? (Y/N)\n")
    if start_choice.lower()[0] == "y":
        p_t("\nThis task isn't for the faint of heart, but we appreciate")
        p_t("your help nonetheless.")
        p_t("We're confident that you're the right person for this job.")
        # Instantiates the player and requests a name and assigns it to
        # a variable.
        player = START_POSITION
        p_t("Forgive my memory, I've dealt with a number of associates")
        p_t("lately.\n")
        player.name = get_str("Could you please state your name again?\n")
        p_t(f"\nVery well, Inspector {player.name}. Let's begin.")
        # Lets the user decide if they want to view the intro scene.
        intro_choice = get_str("\nShall we move onto the briefing? (Y/N):\n")
        if intro_choice.lower()[0] == "y":
            p_t("Play intro scene")
            p_t("This will describe the back story of the Investigator")
            p_t("Their motives, why they approached, who approached them")
            p_t("and ultimately what their goal is")
            p_t("This will lead directly to the start of the game.")
        elif intro_choice.lower()[0] == "n":
            p_t("We'll get straight to it then...")
        else:
            print("Please answer the question, yes or no will suffice.")

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
            command = actions.get_player_command()
            if command["action_type"] == 'MOVE':
                direction = command["direction"]
                player.move(actions.directions[direction])
            elif command["action_type"] == 'EXAMINE':
                # Do make related call
                command = 1

    elif start_choice.lower()[0] == "n":
        p_t("\nPerhaps another person would be better suited.")
        p_t("\nFarewell, Investigator.")
        p_t(END_TITLE)
    else:
        print("\nPlease answer the question, yes or no will suffice.")


start_game()
