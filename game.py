
def p_t(text):
    """
    Print a line of text.
    The function name is abbreviated to permit for longer text strings.
    For clarity: "p_t" stands for print text.
    """
    print(text)


def start_game():
    """
    Starts the game, called at the end of game.py.
    Prints the game logo.
    """
    print("""\033[38;2;150;95;143m
    █████╗ ██╗   ██╗ █████╗ ██████╗ ██╗ ██████╗███████╗
    ██╔══██╗██║   ██║██╔══██╗██╔══██╗██║██╔════╝██╔════╝
    ███████║██║   ██║███████║██████╔╝██║██║     █████╗
    ██╔══██║╚██╗ ██╔╝██╔══██║██╔══██╗██║██║     ██╔══╝
    ██║  ██║ ╚████╔╝ ██║  ██║██║  ██║██║╚██████╗███████╗
    ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝ \n
    """)


start_game()
