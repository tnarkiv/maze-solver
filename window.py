"""Window module of the maze"""
from tkinter import Tk, Canvas


class Window:
    """Window class"""
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze"
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """This function redraws the window"""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """This function keeps the window redrawn till close"""
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        """This function closes the window"""
        self.running = False
