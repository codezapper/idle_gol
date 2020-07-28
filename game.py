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
        self.stdscr.refresh()

    def _read_start(self, filename):
        self._cells = [[' ' for x in range(80)] for y in range(40)]
        try:
            if (filename.endswith(".json")):
                with open(filename, "r") as data_file:
                    for (x, y) in json.load(data_file)["coord"]:
                        self._cells[y][x] = '*'
            else:
                with open(filename, "r") as data_file:
                    rows = data_file.readlines()
                    for y in range(len(self._cells)):
                        for x in range(len(self._cells[0])):
                            self._cells[y][x] = rows[y][x]
        except FileNotFoundError:
            self.stdscr.addstr(0, 0, "Error reading input file")

    def _get_live_neighbours(self, x, y):
        cnt = 0
        if (x < 79) and (self._cells[y][x+1] == '*'):
            cnt += 1
        if (y < 38) and (self._cells[y+1][x] == '*'):
            cnt += 1
        if (x < 79) and (y < 38) and (self._cells[y+1][x+1] == '*'):
            cnt += 1
        if (x > 1) and (self._cells[y][x-1] == '*'):
            cnt += 1
        if (y > 1) and (self._cells[y-1][x] == '*'):
            cnt += 1
        if (x > 1) and (y > 1) and (self._cells[y-1][x-1] == '*'):
            cnt += 1
        if (x < 78) and (y > 1) and (self._cells[y-1][x+1] == '*'):
            cnt += 1
        if (x > 1) and (y < 38) and (self._cells[y+1][x-1] == '*'):
            cnt += 1
        return cnt

    def __init__(self, stdscr, filename="start.data"):
        self.stdscr = stdscr
        self.start_time = time.time() * TIME_MULTIPLIER
        self._draw_grid()
        self._read_start(filename)

    def update(self, key):
        new_cells = [[' ' for x in range(80)] for y in range(40)]
        for y in range(1, 40):
            for x in range(1, 80):
                if (self._cells[y][x] == ' '):
                    if (self._get_live_neighbours(x, y) == 3):
                        new_cells[y][x] = '*'
                else:
                    if (self._get_live_neighbours(x, y) in [2, 3]):
                        new_cells[y][x] = '*'

        self._cells = new_cells
        self._draw_cells()
