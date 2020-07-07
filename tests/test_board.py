import sys
sys.path.append('../')
from game.point import Point
from game.board import Board
from game.status import Status
import unittest



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
