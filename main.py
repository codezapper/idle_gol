import curses
from curses import wrapper
import time

from game import Game


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)

    stdscr.nodelay(True)
    game = Game(stdscr)

    while True:
        key = None
        try:
            key = stdscr.getkey()
        except curses.error:
            pass
        time.sleep(0.03)
        game.update(key)


wrapper(main)
