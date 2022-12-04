"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains helpful functions.
"""

import time


def p_t(text):
    """
    Print a line of text.
    The function name is abbreviated to permit for longer text strings.
    For clarity: "p_t" stands for print text.
    """
    time.sleep(0.75)
    print(text)


def get_str(question):
    """
    Returns a non-empty string, input by the user.
    Runs a while loop, using the "question" parameter to seek user input.
    If an empty string is given (i.e. the user just presses ENTER),
    or if the user inputs only spaces, the loop will print an error message and
    request input again.
    Also removes extra whitespace from strings.
    Adapted from a function by Siobhán Mooney:
    https://github.com/Estelindis/double-agent
    """
    while True:
        input_str = input(f"\033[38;2;191;97;72m{question}\n\033[0m")
        input_str = " ".join(input_str.split())
        if input_str.strip() == "":
            input_str = ""
        if not input_str:
            time.sleep(0.75)
            print("Please input something rather than nothing.\n\n")
        else:
            return input_str


def build_str(str_list):
    """
    Builds a single string from a list of strings.
    """
    full_str = ""
    for line in str_list:
        full_str += f'{line}\n'

    return full_str


def build_nameplate(name):
    """
    Builds a nameplate for a string
    """
    nameplate = ".-" + ("-" * len(name)) + "-.\n"
    nameplate += "| " + name + " |\n"
    nameplate += "'-" + ("-" * len(name)) + "-'\n\n"

    return nameplate
