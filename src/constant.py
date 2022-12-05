"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains global constants.
"""

from player import Player
from position import Position

START_POSITION = Player(Position(2, 0))

START_TITLE = ("""\033[38;2;255;42;42m
 █████╗ ██╗   ██╗ █████╗ ██████╗ ██╗ ██████╗███████╗\033[38;2;254;59;59m
██╔══██╗██║   ██║██╔══██╗██╔══██╗██║██╔════╝██╔════╝\033[38;2;254;78;78m
███████║██║   ██║███████║██████╔╝██║██║     █████╗\033[38;2;255;97;97m
██╔══██║╚██╗ ██╔╝██╔══██║██╔══██╗██║██║     ██╔══╝\033[38;2;255;125;125m
██║  ██║ ╚████╔╝ ██║  ██║██║  ██║██║╚██████╗███████╗\033[38;2;255;155;155m
╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝\033[38;2;255;155;155m\n
\033[0m""")

END_TITLE = ("""\033[38;2;255;42;42m
████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗\033[38;2;254;59;59m
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗\033[38;2;254;78;78m
   ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║\033[38;2;255;97;97m
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║\033[38;2;255;125;125m
   ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔\033[38;2;255;155;155m
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝\033[38;2;255;155;155m
\033[0m""")

INTRO_SCENE = ("""
A few weeks past, you were approached by a mysterious broker
with great financial promise. The end goal is left unclear
as your are told only to gather information from an abandoned
research facility.
Your interest in the reward permits you to accept the task,
considering your strained marriage after the recent passing
of your daughter.
\nBelieving the money will provide a new start, you set out
to the facility.
\nUpon arriving at the designated location, you find it
completely run-down. Despite this, it seems the main
entryway is sealed off. Much of the building is covered in
plantlife. You notice a pipe leading up leading up to a
window in the observatory tower, which you proceed to climb.
Seeing as the window is still locked, you wrap your jacket
around your arm and smash the glass. Your movements begin to
teeter the pipe, and as you scramble in through the window,
the pipe falls down.""")

TUTORIAL_1 = ("""\033[38;2;191;97;72m
.----------.\n| Tutorial |\n'----------'\033[0m\n
When looking for important objects you trust your keen
obervational senses will make IMPORTANT OBJECTS stand out.
\nYour innate ability to orientate yourself will help you keep
track of where you are and what paths are available to you.
Paying attention is key and thankfully you possess an
eye for detail.
\033[38;2;191;97;72m
.----------.\n| Controls |\n'----------'\033[0m\n
Move\n
- You can move in any cardinal direction, so long as the map allows it.
- \033[38;2;191;97;72m"Move South"\033[0m will move you south.
- \033[38;2;191;97;72m"South"\033[0m or \033[38;2;191;97;72m"s"\033[0m, too.
\nExamine\n
- You can examine any object that stands out to you.
- \033[38;2;191;97;72m"Examine PAINT"\033[0m will examine the PAINT.
- \033[38;2;191;97;72m"ex"\033[0m, too.
\nRecall\n
- If you need more details, such as what you first saw when you arrived in a
given area, you can use \033[38;2;191;97;72m"Recall"\033[0m to jog your memory.
- \033[38;2;191;97;72m"r"\033[0m, too.
\033[0m\nHint: Look for capitalised objects, items, and areas to
interact with.""")

BAD_END = ("""Your legs carry you out of the building at full
speed. You think of nothing but to get away from that horrifying
monster. In the end, you came out empty handed, having completely
forgotten why you came into the building in the first place.""")

NEUTRAL_END = ("""You manage to sneak out through the main gate,
having achieved some of your objectives. You're glad to be able
to breathe fresh air again. However, you can't seem to shake the
feeling that you missed something.""")

GOOD_END = ("""You manage to sneak out through the main gate,
ensuring it remains locked afterwards. Documentation in hand,
you're confident that you've solved the building's mysteries.
You head straight to the broker in hopes of them fulfilling
their end of the bargain.""")

CREDITS = ("""Thank you for playing the game!\n
We hope you enjoyed it!\n
\033[38;2;191;97;72m.-----------.\n| Developer |\n'-----------'\033[0m\n
Ryael (aka Andrey B.)\n
\033[38;2;191;97;72m.--------.\n| Writer |\n'--------'\033[0m\n\nLu C.\n
\033[38;2;191;97;72m.--------.\n| Artist |\n'--------'\033[0m\n\nKate V.\n
\033[38;2;191;97;72m.----------------.\n| Special Thanks |\n'----------------'
\033[0m
Simon W., Akshat Garg
Phillip W., Rose S.
Justin Y.""")
