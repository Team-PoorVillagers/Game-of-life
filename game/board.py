from game.cell import Cell
from game.status import Status
from game.point import Point


class Board:
    
    def __init__(self, n, m, points):
        self.rows = n
        self.columns = m
        
        self.board = []
        for i in range(self.rows):
            board_rows = [Cell() for i in range(self.columns)]
            self.board.append(board_rows)

        for point in points:
            self.set_status_of_cell_at_position(point, Status.ALIVE)

    def set_status_of_cell_at_position(self, point, state):
        return self.board[point.X()][point.Y()].set_state(state)

    def get_status_of_cell_at_position(self, point):
        return self.board[point.X()][point.Y()].get_state()

    def get_count_of_alive_neighbours_of_cell(self, point):
        direction_array_x = [1, 1, 0, -1, -1, -1, 0, 1]
        direction_array_y = [0, -1, -1, -1, 0, 1, 1, 1]

        alive_neighbours = 0
        for idx in range(0, len(direction_array_x)):

            neighbour_cell_pos = Point(point.X() + direction_array_x[idx], point.Y() + direction_array_y[idx])

            if self.validate_point(neighbour_cell_pos):
                if self.get_status_of_cell_at_position(neighbour_cell_pos) == Status.ALIVE:
                    alive_neighbours += 1
        
        return alive_neighbours
    
    def validate_point(self, point):
        if 0 <= point.X() < self.rows:
            if 0 <= point.Y() < self.columns:
                return True
            else:
                return False
        else:
            return False
