"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the game-loop.
"""

import actions
import world
from constant import START_POSITION, START_TITLE, END_TITLE, TUTORIAL_1
from constant import INTRO_SCENE, GOOD_END, BAD_END, NEUTRAL_END, CREDITS
from helper import p_t, get_str
from position import Position


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
    while True:
        start_choice = \
            get_str("Investigator, do you accept the task? (Y/N):\n")
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
            p_t(f"\nVery well, Inspector {player.name}. Let's begin.\n")

            # Lets the user decide if they want to view the intro scene.
            while True:
                intro_choice = \
                    get_str("Shall we move onto the briefing? (Y/N):\n")
                if intro_choice.lower()[0] == "y":
                    p_t(INTRO_SCENE)
                    p_t(TUTORIAL_1)
                    break
                elif intro_choice.lower()[0] == "n":
                    p_t("\nWe'll get straight to it then...")
                    break
                else:
                    p_t("\nPlease answer the question, yes or no will suffice."
                        "\n")

            # Spawns the player in the starting room.
            current_room = world.room_at(player.pos)

            while player.pos != Position(0, 1):
                if player.moved:
                    if current_room.visited:
                        p_t("\n" + current_room.description())
                    else:
                        p_t("\n" + current_room.introduction())
                        current_room.visited = True
                # Assigns actions to the player.
                command = actions.get_player_command()
                if command is None:
                    player.moved = False
                    p_t("\nI don't understand that action.\n")
                elif command["action_type"] == 'MOVE':
                    direction = command["direction"]
                    player.move(actions.directions[direction])
                elif command["action_type"] == 'EXAMINE':
                    examined_item = command["item"]
                    player.examine(current_room, examined_item)
                elif command["action_type"] == 'RECALL':
                    player.moved = False
                    p_t("\n" + current_room.introduction())

                current_room = world.room_at(player.pos)

            # Game Endings
            if player.inventory.get_item("Research Documents") and \
                    player.inventory.get_item("Development Records") and \
                    player.inventory.get_item("Security Footage"):
                p_t(GOOD_END)
                p_t(END_TITLE)
                p_t(CREDITS)
            elif player.inventory.get_item("Research Documents") or \
                    player.inventory.get_item("Development Records") or \
                    player.inventory.get_item("Security Footage"):
                p_t(NEUTRAL_END)
                p_t(END_TITLE)
                p_t(CREDITS)
            else:
                p_t(BAD_END)
                p_t(END_TITLE)
                p_t(CREDITS)

            break
        elif start_choice.lower()[0] == "n":
            p_t("\nPerhaps another person would be better suited.")
            p_t("\nFarewell, Investigator.")
            p_t(END_TITLE)
            break
        else:
            print("\nPlease answer the question, yes or no will suffice.\n")


start_game()
