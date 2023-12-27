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

sudoku_puzzle2 = [
    [6, 0, 1, 0, 7, 0, 4, 0, 8],
    [0, 0, 0, 3, 0, 5, 0, 0, 0],
    [0, 7, 0, 1, 0, 8, 0, 5, 0],
    [1, 0, 5, 0, 0, 0, 3, 0, 4],
    [9, 0, 0, 0, 0, 0, 0, 0, 1],
    [7, 0, 4, 0, 0, 0, 6, 0, 9],
    [0, 1, 0, 2, 0, 4, 0, 6, 0],
    [0, 0, 0, 6, 0, 7, 0, 0, 0],
    [2, 0, 7, 0, 1, 0, 8, 0, 0],
]

COUNT = 2
SIZE = 9
EMPTY = 0

def count_possibilities(possibilities_list : List[bool]) :
    count = 0
    for i in range (SIZE) :
        if possibilities_list[i] : 
            count += 1
    return count


class SudokuSolver : 
    def __init__(self, sudoku : List[List[int]]):
        self.possibilities = [[[ True for i in range(SIZE) ] for j in range(SIZE) ] for k in range(SIZE)]
        self.solution = [[ EMPTY for i in range(SIZE) ] for j in range(SIZE) ]
        for i in range(SIZE) : 
            for j in range(SIZE) : 
                cell_value = sudoku[i][j]
                if cell_value != EMPTY :
                    self.place_number(i,j, cell_value)
    
    def place_number(self, x : int, y : int, val : int) :
        self.solution[x][y] = val
        for i in range(SIZE) : 
            self.possibilities[x][i][val - 1] = False
            self.possibilities[i][y][val - 1] = False

        for i in range (SIZE//3) :
            for j in range(SIZE//3) :
                self.possibilities[x//3 * 3 + i][y//3 * 3 + j][val - 1] = False
    
    def can_place_number(self, x : int, y : int, val : int) -> bool:
        return self.solution[x][y] == EMPTY and self.possibilities[x][y][val - 1]

    def cell_with_least_possibilities(self) -> Tuple [int,int,int] | None:
        max = 9
        cell = None
        for i in range (SIZE) :
            for j in range (SIZE) :
                c = count_possibilities(self.possibilities[i][j])
                if self.solution[i][j] == EMPTY and 0 < c and c <= max :
                    max = c
                    cell = (i,j)
        return cell

    def is_solved(self) :
        for i in range (SIZE) :
            for j in range(SIZE) :
                if count_possibilities(self.possibilities[i][j]) > 0 :
                    return False
        return True
                    
    def solve(self) :
        if self.is_solved() :
            return self.solution

        cell = self.cell_with_least_possibilities()
        if not cell : 
            return None
        x, y = cell

        for i in range (1,10) :
            if self.can_place_number(x,y,i) :
                sol = self.solution.copy()
                pos = self.possibilities.copy()
                self.place_number(x,y,i)
                self.trivial_moves()
                if self.solve() != None :
                    return self.solution
                self.solution = sol
                self.possibilities = pos
        return None

    def trivial_moves(self) :
        changed = True
        while changed : 
            changed = False
            for i in range(SIZE) :
                for j in range(SIZE) :
                    if self.is_trivial(i,j) :
                        changed = True
                        val = self.possibilities[i][j].index(True)
                        self.place_number(i,j,val + 1)

    def is_trivial(self, x : int, y : int) :
        return count_possibilities(self.possibilities[x][y]) == 1 and not self.solution[x][y]


solver = SudokuSolver(sudoku_puzzle2)
print(solver.solve())
