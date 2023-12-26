import time
from typing import Tuple,List
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

SIZE=9
EMPTY=0
FILLED=1
ROW=True
COL=False

class SudokuSolver :
    def __init__(self, starter : List[List[int]]) :
        self.solution =  
        self.bitmap = 
        self.set_empty_cells()

    @property
    def board(self) :
        return self._board

    @board.setter
    def board(self, b : List[List[int]]) :
        self._board = b

    def set_empty_cells (self) :
        for i in range (SIZE) :
            for j in range (SIZE) :
                if self._board[i][j] == EMPTY :
                    self._empty_cells.append((i,j))

    def board_valid (self) -> bool:
        for i in range(SIZE) :
                if not (self._line_valid(i, ROW) and self._line_valid(i, COL)) :
                    return False
        for i in range(SIZE//3) :
            for j in range(2) : 
                if not self._box_valid(i * 3, j * 3) :
                    return False
        return True

    def _line_valid (self, pos : int, row : bool) -> bool:
        in_pos = [EMPTY] * 10
        for i in range (SIZE) : 
            cell_value = self.board[i][pos] if row else self.board[pos][i]
            if cell_value != EMPTY and in_pos[cell_value] :
                return False
            in_pos[cell_value] = FILLED
        return True

    def _box_valid (self, offset_x : int, offset_y : int) -> bool:
        in_box = [EMPTY] * 10
        for i in range (SIZE//3) :
            for j in range (SIZE//3) :
                cell_value = self._board[offset_x + i][offset_y + j]
                if cell_value != EMPTY and in_box[cell_value] :
                    return False
                in_box[cell_value] = FILLED
        return True

    def solve(self) -> bool:
        if not self.board_valid() : 
            return False
        if not self._empty_cells :
            return True
        next = self._empty_cells.pop()
        x, y = next 

        for i in range (SIZE) :
            self._board[x][y] = i + 1
            if self.solve() :
                return True
            self._board[x][y] = EMPTY
        self._empty_cells.append(next)

        return False

