import re
import random
import os
from time import sleep


COLORS = [
    31,
    33,
    35,
    36
]


def get_tree():
    tree = '\033[32m'
    tree += r'''
       X
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
    return tree


def main():
    print("\033[?25l", flush=True)
    for _ in range(5):
        os.system('clear')
        tree = get_tree()
        tree = re.sub("o", lambda _: f'\033[{COLORS[random.randint(0, len(COLORS)-1)]}mo\033[32m', tree)
        tree = re.sub("X", r'\033[33mX\033[32m', tree)
        print(tree)
        sleep(0.5)
    print("\033[?25h", flush=True)


if __name__ == '__main__':
    main()
