import unittest
import sys
sys.path.append('../')

from game.cell import Cell

class TestCellClass(unittest.TestCase):

    def test_initialized_cell_is_dead(self):
        new_cell = Cell()
        self.assertFalse(new_cell.get_state())
