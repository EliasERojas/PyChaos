from copy import deepcopy
from time import time
from collections import deque
from random import choice,randint,shuffle
from typing import Tuple,List

sudoku6 = [
    [1, 0, 0, 0, 0, 0, 0, 1, 3],
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [2, 0, 0, 0, 6, 0, 0, 0, 0],
    [9, 0, 6, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 3, 0, 1, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 4, 0, 7, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

sudoku0 = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

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
    [0, 0, 1, 0, 7, 0, 4, 0, 8],
    [0, 0, 0, 3, 0, 5, 0, 0, 0],
    [0, 7, 0, 1, 0, 8, 0, 5, 0],
    [1, 0, 5, 0, 0, 0, 3, 0, 4],
    [9, 0, 0, 0, 0, 0, 0, 0, 1],
    [7, 0, 4, 0, 0, 0, 6, 0, 9],
    [0, 1, 0, 2, 0, 4, 0, 6, 0],
    [0, 0, 0, 6, 0, 7, 0, 0, 0],
    [2, 0, 7, 0, 1, 0, 8, 0, 0],
]

sudoku_puzzle3 = [
    [1, 0, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 3, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 3, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 7, 5],
    [0, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 6, 0, 0],
]

sudoku7 = [
    [0, 0, 0, 0, 0, 0, 4, 0, 8],
    [0, 0, 1, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 9, 7, 0],
    [5, 0, 8, 9, 0, 1, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 2, 8, 0, 3, 0],
    [8, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 5, 0, 0],
    [0, 6, 2, 8, 9, 0, 0, 0, 0]
]


COUNT = 2
SIZE = 9
THIRD_SIZE = 3
EMPTY = 0
maskval = (511,510,509,507,503,495,479,447,383,255)
bitval = (0,1,2,4,8,16,32,64,128,256)

def count_bits(n) :
    count = 0
    while n :
        count += n & 1
        n >>= 1
    return count

class SudokuSolver : 
    def __init__(self, sudoku : List[List[int]] | None = None):
        self.possibilities = [[511 for j in range(SIZE) ] for k in range(SIZE)]
        self.solution = [[ EMPTY for i in range(SIZE) ] for j in range(SIZE) ]
        self.placed = 0
        for i in range(SIZE) : 
            for j in range(SIZE) : 
                cell_value = sudoku[i][j]
                if cell_value != EMPTY :
                    self.place_number(i,j, cell_value)

    def place_number(self, x : int, y : int, val : int) :
        self.solution[x][y] = val
        self.placed += 1
        self.possibilities[x][y] = 0
        mask = maskval[val]
        for i in range(SIZE) : 
            self.possibilities[x][i] &= mask
            self.possibilities[i][y] &= mask

        for i in range (THIRD_SIZE) :
            for j in range(THIRD_SIZE) :
                self.possibilities[x//3 * 3 + i][y//3 * 3 + j] &= mask

    def place_single_possibility(self) :
        for val in range(1,10) :
            bit = bitval[val]

            for i in range (SIZE) :
                col = -1
                for j in range(SIZE) :
                    if self.possibilities[i][j] & bit > 0 :
                        if col < 0:
                            col = j
                        else : 
                            col = -1
                            break
                if col >= 0 :
                    self.place_number(i, col, val)

            for i in range (SIZE) :
                row = -1 
                for j in range(SIZE) :
                    if self.possibilities[j][i] & bit > 0 :
                        if row < 0:
                            row = j
                        else :
                            row = -1
                            break
                if row >= 0:
                    self.place_number(row, i, val)

    def boxes_single_possibility(self) :
        for i in range(0,SIZE,THIRD_SIZE) :
            for j in range(0,SIZE,THIRD_SIZE) :
                for val in range(1,10) :
                    pair = self.box_single_possibility(i,j,val)
                    if pair[0] >= 0 :
                        self.place_number(pair[0],pair[1],val)

    def box_single_possibility(self, x, y, val): 
        bit = bitval[val]
        row = -1
        col = -1
        for i in range(THIRD_SIZE) :
            for j in range(THIRD_SIZE) :
                if (self.possibilities[x + i][y + j] & bit) > 0 :
                    if row < 0 :
                        row = x + i
                        col = y + j
                    else :
                        row = -1
                        return (row,col)
        return (row,col)

    def solve(self) :
        before = -1
        while (self.placed - before) > 0 : 
            self.trivial_moves()
            self.boxes_single_possibility()
            self.place_single_possibility()

        if self.placed < 81 :
            if self.brute_force() : 
                return self.solution
            return None

        return self.solution

    def brute_force(self) :
        x, y = self.least_possibilities_cell()
        for val in range (1,10) :
            bit = bitval[val]
            if self.possibilities[x][y] & bit > 0 :
                sol_copy = deepcopy(self.solution)
                pos_copy = deepcopy(self.possibilities)
                placed_copy = self.placed
                self.place_number(x,y,val)
                self.solve()
                if self.placed == 81 :
                    return True
                self.possibilities = pos_copy
                self.solution = sol_copy
                self.placed = placed_copy
        return False

    def brute_force2(self) :
        for i in range(SIZE) :
            for j in range (SIZE) :
                for val in range(1,10) :
                    bit = bitval[val]
                    if (self.possibilities[i][j] & bit) > 0 :
                        sol_copy = deepcopy(self.solution)
                        pos_copy = deepcopy(self.possibilities)
                        placed_copy = self.placed
                        self.place_number(i,j,val)
                        self.solve()
                        if self.placed == 81 :
                            return True
                        self.possibilities = pos_copy
                        self.solution = sol_copy
                        self.placed = placed_copy
                    return False
        return False

    def least_possibilities_cell(self) :
        x = 0
        y = 0
        min = SIZE
        for i in range(SIZE) :
            for j in range(SIZE) :
                c = count_bits(self.possibilities[i][j])
                if c and c < min :
                    min = c
                    x = i
                    y = j
        return (x,y)
                

    def trivial_moves(self) :
        for i in range(SIZE) :
            for j in range(SIZE) :
                if count_bits(self.possibilities[i][j]) == 1 :
                    self.set_trivial(i,j)

    def set_trivial(self, x, y) :
        p = self.possibilities[x][y] 
        num = 0
        while p :
            p >>= 1
            num += 1
        self.place_number(x, y, num)

start = time()
solver = SudokuSolver(sudoku6)
print(solver.solve())
end = time()
print(end - start)
