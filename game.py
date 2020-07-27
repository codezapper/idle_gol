import json
import time

TIME_MULTIPLIER = 1000000


class Game:
    def _draw_grid(self):
        rows, cols = (41, 80) #self.stdscr.getmaxyx()
        self.stdscr.addstr(0, 0, u'\u2554')
        self.stdscr.addstr(0, cols, u'\u2557')
        self.stdscr.addstr(rows - 1, 0, u'\u255a')
        self.stdscr.addstr(rows - 1, cols, u'\u2568')
        for row in range(1, rows - 1):
            self.stdscr.addstr(row, 0, u'\u2551')
            self.stdscr.addstr(row, cols, u'\u2551')
        self.stdscr.addstr(0, 1, u'\u2550' * (cols - 1))
        self.stdscr.addstr(rows - 1, 1, u'\u2550' * (cols - 1))
        self.stdscr.refresh()

    def _draw_cells(self):
        for y in range(1, 40):
            for x in range(1, 80):
                self.stdscr.addstr(y, x, self._cells[y][x])

    def _read_start(self, filename):
        self._cells = [[' ' for x in range(80)] for y in range(40)]
        with open(filename, "r") as data_file:
            for (x, y) in json.load(data_file)["coord"]:
                self._cells[x][y] = '*'

    def __init__(self, stdscr, filename="start.json"):
        self.stdscr = stdscr
        self.start_time = time.time() * TIME_MULTIPLIER
        self._draw_grid()
        self._read_start(filename)

    def update(self, key):
        self._draw_cells()
