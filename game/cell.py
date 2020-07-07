from game.status import Status


class Cell:
    def __init__(self):
        self.state = Status.DEAD

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
