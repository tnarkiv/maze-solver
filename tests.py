"""Testing Module"""

import unittest

from cell import Cell
from maze import Maze


class Tests(unittest.TestCase):
    """Contains unit tests"""

    def test_maze_create_cells(self):
        """Tests the creation of cells in a maze"""
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_maze_cells_are_initialized(self):
        """Tests initialization of cells"""
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        for row in m1.cells:
            for cell in row:
                self.assertIsInstance(cell, Cell)

    def test_maze_cell_walls_are_varied(self):
        """Tests whether cells have different walls"""
        num_cols = 4
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        wall_configs = set()

        for row in m1.cells:
            for cell in row:
                wall_configs.add(
                    (
                        cell.has_left_wall,
                        cell.has_right_wall,
                        cell.has_top_wall,
                        cell.has_bottom_wall,
                    )
                )

        self.assertGreater(len(wall_configs), 1)

    def test_maze_cell_positions(self):
        """Test the positioning of the cells"""
        num_cols = 3
        num_rows = 3
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        first_cell = m1.cells[0][0]
        self.assertEqual(first_cell.x1, 0)
        self.assertEqual(first_cell.y1, 0)
        self.assertEqual(first_cell.x2, 10)
        self.assertEqual(first_cell.y2, 10)

        last_cell = m1.cells[2][2]
        self.assertEqual(last_cell.x1, 20)
        self.assertEqual(last_cell.y1, 20)
        self.assertEqual(last_cell.x2, 30)
        self.assertEqual(last_cell.y2, 30)


if __name__ == "__main__":
    unittest.main()
