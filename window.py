"""Window module of the maze"""

from tkinter import Tk, Canvas

from line import Line


class Window:
    """Window class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze"
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """This function redraws the window"""
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        """This function keeps the window redrawn till close"""
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        """This function closes the window"""
        self.running = False

    def draw_line(self, line: Line, fill_color: str):
        """This function draws a line in the window

        Args:
            line (Line): Line
            fill_color (str): Color of line
        """
        line.draw(self.canvas, fill_color)
