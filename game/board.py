from game.cell import Cell
from game.status import Status

class Board:
    
    def __init__(self, n, m, points):
        self.rows = n
        self.columns = m
        
        self.board = []
        for i in range(self.rows):
            board_rows = [Cell() for i in range(self.columns)]
            self.board.append(board_rows)

        for i in range(len(points)):
            self.board[points[i].X()][points[i].Y()].set_state(Status.ALIVE)
