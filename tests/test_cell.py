import unittest
import sys
sys.path.append('../')

from game.cell import Cell

class TestCellClass(unittest.TestCase):

    def test_initialized_cell_is_dead(self):
        new_cell = Cell()
        self.assertFalse(new_cell.get_state())

    def test_setting_up_cell_state_as_true(self):
        new_cell = Cell()
        new_cell.set_state(True)
        self.assertTrue(new_cell.get_state())
    
    def test_setting_up_cell_state_as_false(self):
        new_cell = Cell()
        new_cell.set_state(False)
        self.assertFalse(new_cell.get_state())
        