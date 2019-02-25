import os
import data_manager
import ui


MOVE = {"FORWARD": 1, "BACKWARD": -1}


def get_char_in_terminal():
    """
    Get character from user in terminal, when he push the button.
    :return: char: keyboard character
    """
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char


def move_hero():
    ui.show_map(level_map)
    
    while True:
        if get_char_in_terminal() == "w":
            ui.show_map()
            os.system("clear")
            #HERO_POS[0] += 1
            HERO_POS[1] -= 1
        print(HERO_POS[0], HERO_POS[1])
        maps[HERO_POS[1]][HERO_POS[0]] = "@"


    

move_hero()
