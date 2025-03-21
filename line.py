"""Line module"""

from tkinter import Canvas
import point


class Line:
    """Line class"""

    def __init__(self, a: point, b: point):
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: str):
        """Draws

        Args:
            canvas (Canvas): Canvas on which maze will be drawn
            fill_color (string): Color of the line
        """
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
        )
