import fileinput
from typing import List

# Move all rocks to the north and calculate load
# utilizar w a s d y pedri entradas para mover las piedras

# def tilt_north(dish:List[List[str]]) : 
#     for i in range(0,SIZE) :
#         e, r = -1 , 0
#         while r < SIZE :
#             if dish[r][i] == ROUNDED :
#                 e += 1
#                 dish[r][i]= EMPTY
#                 dish[e][i] = ROUNDED
#             elif dish[r][i] == CUBED :
#                 e = r
#             r += 1
# 
# def tilt_south(dish:List[List[str]]) : 
#     for i in range(0,SIZE) :
#         e, r = -1 , 0
#         while r < SIZE :
#             if dish[SIZE - 1 -r][i] == ROUNDED :
#                 e += 1
#                 dish[SIZE - 1 - r][i]= EMPTY
#                 dish[SIZE - 1 - e][i] = ROUNDED
#             elif dish[SIZE - 1 - r][i] == CUBED :
#                 e = r
#             r += 1

ROUNDED = "O"
EMPTY = "."
CUBED = "#"

dish = [
    ['O', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
    ['O', '.', 'O', 'O', '#', '.', '.', '.', '.', '#'], 
    ['.', '.', '.', '.', '.', '#', '#', '.', '.', '.'], 
    ['O', 'O', '.', '#', 'O', '.', '.', '.', '.', 'O'], 
    ['.', 'O', '.', '.', '.', '.', '.', 'O', '#', '.'], 
    ['O', '.', '#', '.', '.', 'O', '.', '#', '.', '#'], 
    ['.', '.', 'O', '.', '.', '#', 'O', '.', '.', 'O'], 
    ['.', '.', '.', '.', '.', '.', '.', 'O', '.', '.'], 
    ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'], 
    ['#', 'O', 'O', '.', '.', '#', '.', '.', '.', '.'], 
] 
# para mover hacia el oeste, voy desde el oeste llevando piedras
# hasta que alcancen un limite (debo marcar que piedra comence a mover)


blua_lipa = ['O', '.', 'O', '.', '.', '#', '.', '.', '.', 'O']


SIZE = 10
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

def tilt_vertically(dish : List[List[str]], dir : int) :
    offset = SIZE-1 if dir == SOUTH else 0
    # -1 goes SOUTH, 1 goes NORTH
    coefficient = -1 if dir == SOUTH else 1
    for i in range(0,SIZE):
        e, r = -1 , 0
        while r < SIZE :
            row_rock = offset + coefficient * r
            if dish[row_rock][i] == ROUNDED :
                dish[row_rock][i] = EMPTY
                e += 1
                row_empty = offset + coefficient * e
                dish[row_empty][i] = ROUNDED
            elif dish[row_rock][i] == CUBED :
                e = r
            r += 1

def tilt_horizontally(dish : List[List[str]], dir : int) :
    offset = SIZE-1 if dir == EAST else 0
    # -1 goes EAST, 1 goes WEST
    coefficient = -1 if dir == EAST else 1
    for i in range(0,SIZE):
        e, r = -1 , 0
        while r < SIZE :
            col_rock = offset + coefficient * r
            if dish[i][col_rock] == ROUNDED :
                dish[i][col_rock] = EMPTY
                e += 1
                col_empty = offset + coefficient * e
                dish[i][col_empty] = ROUNDED
            elif dish[i][col_rock] == CUBED :
                e = r
            r += 1


def print_dish(dish : List[List[str]]) : 
    if not dish :
        return
    for row in dish :
        for rock in row :
            print(rock, " ", end=" ")
        print()

