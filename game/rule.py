from game.cell import Status
from game.constant import Constants


class Rule:

    @staticmethod
    def get_state_in_next_generation(current_status, count_of_live_neighbours):
        if current_status == Status.ALIVE:
            return Status.ALIVE if count_of_live_neighbours in [Constants.THREE, Constants.TWO] else Status.DEAD
        else:
            return Status.ALIVE if count_of_live_neighbours == Constants.THREE else Status.DEAD
