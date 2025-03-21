"""Main module of the program"""

import random
import time
from line import Line
from point import Point
from window import Window


def main():
    """Main function"""
    win = Window(800, 600)
    a_s, b_s = [], []
    for i in range(50):
        a_s.append(Point(random.randint(0, 400), random.randint(0, 300)))
        b_s.append(Point(a_s[i].x + 150, a_s[i].y + 150))
    colors = ["red", "blue", "green", "yellow", "purple"]
    for i in range(50):
        win.draw_line(Line(a_s[i], b_s[i]), colors[i % len(colors)])
        win.redraw()
        time.sleep(0.1)
    win.wait_for_close()


main()
