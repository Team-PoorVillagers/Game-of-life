import unittest
import sys
from game.status import Status

sys.path.append('../')

from game.cell import Cell


class TestCellClass(unittest.TestCase):

    def test_initialized_cell_is_dead(self):
        new_cell = Cell()
        self.assertEqual(Status.DEAD, new_cell.get_state())

    def test_setting_up_cell_state_as_alive(self):
        new_cell = Cell()
        new_cell.set_state(Status.ALIVE)
        self.assertEqual(Status.ALIVE, new_cell.get_state())

    def test_setting_up_cell_state_as_false(self):
        new_cell = Cell()
        new_cell.set_state(False)
        self.assertFalse(new_cell.get_state())
