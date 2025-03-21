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
        win : Window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        """This function draws a cell"""
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(line, "red")
        if self.has_top_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
            self._win.draw_line(line, "red")
