# Inspiration: https://www.youtube.com/watch?v=NENq-G2PsTo

import random
from time import sleep
from ansi import Ansi


def get_tree():
    """Return a green tree template as a string."""
    tree = Ansi.GREEN
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
    tree += Ansi.RESET
    return tree


def colorize_tree(tree):
    """Return the tree string with ornaments and star colorized."""
    tree_list = list(tree)
    ornament_indices = [i for i, c in enumerate(tree) if c == 'o']
    star_index = tree_list.index('*')

    for i in ornament_indices:
        tree_list[i] = f'{random.choice(Ansi.LIGHT_COLORS)}o{Ansi.GREEN}'
    tree_list[star_index] = f'{Ansi.YELLOW}*{Ansi.GREEN}'

    return ''.join(tree_list)


def clear_screen():
    """Clear the screen and place the cursor at the top left."""
    print(Ansi.CLEAR_SCREEN + Ansi.CURSOR_HOME, end='')


def main():
    print(Ansi.HIDE_CURSOR)
    for _ in range(10):
        clear_screen()
        colorized_tree = colorize_tree(get_tree())
        print(colorized_tree)
        sleep(0.5)

    clear_screen()
    print(Ansi.SHOW_CURSOR)


if __name__ == '__main__':
    main()
