import unittest
import sys

sys.path.append('../')
from game.status import Status
from game.rule import Rule


class TestRuleClass(unittest.TestCase):

    def test_alive_entity_with_more_than_three_live_neighbours_treated_as_dead(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.ALIVE, 5)
        expected_future_state = Status.DEAD
        self.assertEqual(expected_future_state, actual_future_state)

    def test_alive_entity_with_less_than_two_live_neighbours_treated_as_dead(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.ALIVE, 1)
        expected_future_state = Status.DEAD
        self.assertEqual(expected_future_state, actual_future_state)

    def test_alive_entity_with_three_live_neighbours_treated_as_alive(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.ALIVE, 3)
        expected_future_state = Status.ALIVE
        self.assertEqual(expected_future_state, actual_future_state)

    def test_alive_entity_with_two_live_neighbours_treated_as_alive(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.ALIVE, 2)
        expected_future_state = Status.ALIVE
        self.assertEqual(expected_future_state, actual_future_state)

    def test_dead_entity_with_three_live_neighbours_treated_as_alive(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.DEAD, 3)
        expected_future_state = Status.ALIVE
        self.assertEqual(expected_future_state, actual_future_state)

    def test_dead_entity_with_less_than_three_live_neighbours_treated_as_dead(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.DEAD, 2)
        expected_future_state = Status.DEAD
        self.assertEqual(expected_future_state, actual_future_state)

    def test_dead_entity_with_more_than_three_live_neighbours_treated_as_dead(self):
        actual_future_state = Rule.get_state_in_next_generation(Status.DEAD, 5)
        expected_future_state = Status.DEAD
        self.assertEqual(expected_future_state, actual_future_state)
