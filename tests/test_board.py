import unittest
from game.status import Status
from game.board import Board
from game.point import Point
import sys
sys.path.append('../')


class TestBoardClass(unittest.TestCase):

    def test_initial_state_of_board(self):

        sample_row = 3
        sample_columns = 3
        sample_points = [Point(0, 0), Point(0, 2)]

        obj = Board(sample_row, sample_columns, sample_points)

        for i in range(len(sample_points)):
            actual_status = obj.board[sample_points[i].X(
            )][sample_points[i].Y()].get_state()
            expected_status = Status.ALIVE
            self.assertEqual(expected_status, actual_status)

    def test_validate_point(self):

        sample_row = 2
        sample_columns = 4
        sample_alive_points = []

        obj = Board(sample_row, sample_columns, sample_alive_points)

        self.assertTrue(obj.validate_point(Point(1, 3)))
        self.assertFalse(obj.validate_point(Point(1, 5)))

    def test_get_count_of_alive_neighbours_of_cell(self):

        sample_row = 2
        sample_columns = 4
        sample_alive_points = [Point(0, 0), Point(1, 1)]

        obj = Board(sample_row, sample_columns, sample_alive_points)
        test_point = Point(0, 0)
        expected_alive_neighbours = 1
        self.assertEqual(obj.get_count_of_alive_neighbours_of_cell(
            test_point), expected_alive_neighbours)
