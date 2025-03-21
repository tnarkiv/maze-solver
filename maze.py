"""Maze module"""

import random
import time
from cell import Cell


class Maze:
    """Maze class"""

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()

    def _create_cells(self):
        self.cells = [
            [None for _ in range(self.num_cols)] for _ in range(self.num_rows)
        ]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
        if self.win:
            self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        has_left_wall = random.choice([True, False])
        has_right_wall = random.choice([True, False])
        has_top_wall = random.choice([True, False])
        has_bottom_wall = random.choice([True, False])

        self.cells[i][j] = Cell(
            x1,
            x2,
            y1,
            y2,
            self.win,
            has_left_wall,
            has_right_wall,
            has_top_wall,
            has_bottom_wall,
        )

        if not self.win:
            return

        self.cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].draw()

        self.cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self.cells[self.num_rows-1][self.num_cols-1].draw()

        self._animate()
