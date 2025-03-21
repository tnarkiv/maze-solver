"""Main module of the program"""

import random
import time
from cell import Cell
from point import Point
from window import Window


def main():
    """Main function"""
    win = Window(800, 600)
    a_s, b_s = [], []
    for i in range(50):
        a_s.append(Point(random.randint(0, 400), random.randint(0, 300)))
        b_s.append(Point(a_s[i].x + 150, a_s[i].y + 150))
    for i in range(50):
        cell = Cell(
            a_s[i].x,
            b_s[i].x,
            a_s[i].y,
            b_s[i].y,
            win,
            has_left_wall=random.choice([True, False]),
            has_right_wall=random.choice([True, False]),
            has_top_wall=random.choice([True, False]),
            has_bottom_wall=random.choice([True, False]),
        )
        cell.draw()
        win.redraw()
        time.sleep(0.1)
    win.wait_for_close()


main()
