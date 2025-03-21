"""Cell module"""

from line import Line
from point import Point
from window import Window


class Cell:
    """Cell class"""

    def __init__(
        self,
        x1,
        x2,
        y1,
        y2,
        win: Window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win

    def draw(self):
        """This function draws a cell"""
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y2), Point(self.x2, self.y1))
            self.win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x1, self.y1))
            self.win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        """This function draws a path between the centers of two cells

        Args:
            to_cell (Cell): Destination cell
            undo (bool, optional): Highlights backtracking. Defaults to False.
        """
        c1, c2 = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2), Point(
            (to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2
        )
        if undo:
            self.win.draw_line(Line(c1, c2), "gray")
        else:
            self.win.draw_line(Line(c1, c2), "red")
