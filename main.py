# Inspiration: https://www.youtube.com/watch?v=NENq-G2PsTo

import random
from time import sleep

# ANSI escape sequences
ANSI = {
    'HIDE_CURSOR': '\033[?25l',
    'SHOW_CURSOR': '\033[?25h',
    'CLEAR_SCREEN': '\033[2J',
    'CURSOR_HOME': '\033[H',
    'RESET': '\033[0m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'LIGHT_COLORS': [
        '\033[31m',  # red
        '\033[33m',  # yellow
        '\033[35m',  # magenta
        '\033[36m'   # cyan
    ]
}


def get_tree():
    """Return a green tree template as a string."""
    tree = ANSI['GREEN']
    tree += r'''
       *
      / \
     /o  \
    /_ o _\
    /    o\
   / o  o  \
  /_     o _\
  /  o   o  \
 /  o  o    o\
/_____________\
      |||
'''
    tree += ANSI['RESET']
    return tree


def colorize_tree(tree):
    """Return the tree string with ornaments and star colorized."""
    tree_list = list(tree)
    ornament_indices = [i for i, c in enumerate(tree) if c == 'o']
    star_index = tree_list.index('*')

    for i in ornament_indices:
        tree_list[i] = f"{random.choice(ANSI['LIGHT_COLORS'])}o{ANSI['GREEN']}"
    tree_list[star_index] = f"{ANSI['YELLOW']}*{ANSI['GREEN']}"

    return ''.join(tree_list)


def clear_screen():
    """Clear the screen and place the cursor at the top left."""
    print(ANSI['CLEAR_SCREEN'] + ANSI['CURSOR_HOME'], end='')


def main():
    print(ANSI['HIDE_CURSOR'])
    for _ in range(10):
        clear_screen()
        print(colorize_tree(get_tree()))
        sleep(0.5)

    clear_screen()
    print(ANSI['SHOW_CURSOR'])


if __name__ == '__main__':
    main()
