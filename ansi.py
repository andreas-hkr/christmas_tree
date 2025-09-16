class Ansi:
    HIDE_CURSOR = '\033[?25l'
    SHOW_CURSOR = '\033[?25h'
    CLEAR_SCREEN = '\033[2J'
    CURSOR_HOME = '\033[H'
    RESET = '\033[0m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    LIGHT_COLORS = [
        '\033[31m',  # red
        '\033[33m',  # yellow
        '\033[35m',  # magenta
        '\033[36m'   # cyan
    ]
