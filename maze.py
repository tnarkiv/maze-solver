"""Maze module"""

import random
import time
from cell import Cell


class Maze:
    """Maze class"""

    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
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
        if not seed:
            random.seed(seed)

    def _create_cells(self):
        self.cells = [
            [None for _ in range(self.num_cols)] for _ in range(self.num_rows)
        ]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
        if self.win:
            self._break_walls_r(0, 0)
            self._break_entrance_and_exit()
            self._reset_cells_visited()

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

        self.cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.cells[self.num_rows - 1][self.num_cols - 1].draw()

        self._animate()

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < self.num_rows
                and 0 <= nj < self.num_cols
                and not self.cells[ni][nj].visited
            ):
                if di == -1:
                    self.cells[i][j].has_top_wall = False
                    self.cells[ni][nj].has_bottom_wall = False
                elif di == 1:
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[ni][nj].has_top_wall = False
                elif dj == -1:
                    self.cells[i][j].has_left_wall = False
                    self.cells[ni][nj].has_right_wall = False
                elif dj == 1:
                    self.cells[i][j].has_right_wall = False
                    self.cells[ni][nj].has_left_wall = False

                self.cells[i][j].draw()
                self.cells[ni][nj].draw()
                self._animate()
                self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        if i == (self.num_rows - 1) and j == (self.num_cols - 1):
            return True

        self._animate()
        self.cells[i][j].visited = True

        directions = [
            (-1, 0, "has_top_wall", "has_bottom_wall"),
            (1, 0, "has_bottom_wall", "has_top_wall"),
            (0, -1, "has_left_wall", "has_right_wall"),
            (0, 1, "has_right_wall", "has_left_wall"),
        ]

        for di, dj, wall1, wall2 in directions:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < self.num_rows
                and 0 <= nj < self.num_cols
                and not self.cells[ni][nj].visited
            ):
                if not getattr(self.cells[i][j], wall1) and not getattr(
                    self.cells[ni][nj], wall2
                ):
                    self.cells[i][j].draw_move(self.cells[ni][nj])
                    if self._solve_r(ni, nj):
                        return True
                    self.cells[i][j].draw_move(self.cells[ni][nj], undo=True)

        return False
