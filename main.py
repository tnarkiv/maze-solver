"""Main module of the program"""

from maze import Maze
from window import Window


def main():
    """Main function"""
    win = Window(800, 600)
    maze = Maze(0, 0, 20, 20, 40, 30, win, 1)
    maze.solve()
    win.wait_for_close()


main()
