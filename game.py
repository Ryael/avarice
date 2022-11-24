"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the game-loop and global variables.
"""

game = {
    "name": ""
}


def p_t(text):
    """
    Print a line of text.
    The function name is abbreviated to permit for longer text strings.
    For clarity: "p_t" stands for print text.
    """
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
    start_choice = get_str("Investigator, do you accept the task? (Y/N):")
    if start_choice.lower() == "y" or start_choice.lower() == "yes":
        p_t("This task isn't for the faint of hearted,")
        p_t("but we appreciate your help in this matter.")
        p_t("We're sure you're the right person for this job.")
        # Requests a name and saves it in the "game" dictionary.
        game["name"] = get_str("Could you please state your name again?")
        p_t(f"Very well, Inspector {game['name']}. Let's begin.")
        # Lets the user decide if they want to view the intro scene.
        view_intro = False
        while not view_intro:
            intro_choice = get_str("Would you like to see the intro? (Y/N):")
            if intro_choice.lower() == "yes" or intro_choice.lower() == "y":
                p_t("Play intro scene")
                p_t("This will describe the back story of the Investigator")
                p_t("Their motives, why they approached, who approached them")
                p_t("and ultimately what their goal is")
                p_t("This will lead directly to the start of the game.")
                first_scene()
            elif intro_choice.lower() == "no" or intro_choice.lower() == "n":
                first_scene()
            else:
                print("Please answer the question, yes or no will suffice.")
    elif start_choice.lower() == "n" or start_choice.lower() == "no":
        p_t("""\033[38;2;150;95;143m
    ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗
    ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
       ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║
       ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
       ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔
            \033[0m\n""")
        p_t("Perhaps another person would be better suited.")
        p_t("Farewell, Investigator.")
    else:
        print("Please answer the question, yes or no will suffice.")


start_game()
