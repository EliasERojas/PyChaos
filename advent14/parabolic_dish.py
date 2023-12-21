from typing import List
from random import randrange
import os
import time

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

EXIT = 4
NORTH = 2
SOUTH = 1
EAST = 3
WEST = 0

class DishGame : 
    def __init__(self, size):
        self.__dish : List[List[str]]= [] 
        self.__dir : int = NORTH
        self.__size : int = size
        self.__initialize_dish()

    def print_dish(self) : 
        if not self.__dish :
            return
        for row in self.__dish :
            for slot in row :
                print(slot, " ", end=" ")
            print()

    def __initialize_dish(self) :
        for i in range (0,self.__size) : 
            self.__dish.append([])
            for j in range (0, self.__size) : 
                slot = EMPTY
                magic_num = randrange(0,100)
                if magic_num < 10 : 
                    slot = ROUNDED
                elif magic_num < 30 :
                    slot = CUBED
                self.__dish[i].append(slot)

    def tilt(self, dir : int) : 
        self.__dir = dir
        if dir == SOUTH or dir == NORTH :
            self.__tilt_vertically()
        elif dir == WEST or dir == EAST : 
            self.__tilt_horizontally()
        else : 
            raise ValueError("Direction must be a cardinal point")


    def __tilt_vertically(self) :
        offset = self.__size-1 if self.__dir == SOUTH else 0
        # -1 goes SOUTH, 1 goes NORTH
        coefficient = -1 if self.__dir == SOUTH else 1
        for i in range(0,self.__size):
            e, r = -1 , 0
            while r < self.__size :
                row_rock = offset + coefficient * r
                if self.__dish[row_rock][i] == ROUNDED :
                    self.__dish[row_rock][i] = EMPTY
                    e += 1
                    row_empty = offset + coefficient * e
                    self.__dish[row_empty][i] = ROUNDED
                elif self.__dish[row_rock][i] == CUBED :
                    e = r
                r += 1


    def __tilt_horizontally(self) :
        offset = self.__size-1 if self.__dir == EAST else 0
        # -1 goes EAST, 1 goes WEST
        coefficient = -1 if self.__dir == EAST else 1
        for i in range(0,self.__size):
            e, r = -1 , 0
            while r < self.__size :
                col_rock = offset + coefficient * r
                print(col_rock)
                if self.__dish[i][col_rock] == ROUNDED :
                    self.__dish[i][col_rock] = EMPTY
                    e += 1
                    col_empty = offset + coefficient * e
                    self.__dish[i][col_empty] = ROUNDED
                elif self.__dish[i][col_rock] == CUBED :
                    e = r
                r += 1

dish = DishGame(25)
user_input = 0

while user_input != EXIT :
    os.system("clear")
    try :
        dish.print_dish()
        user_input = input("Dir (1 = W, 2 = S, 3 = E, 4 = E, 5 = Exit) :")
        a = int(user_input) - 1
        if a == EXIT : 
            break
        dish.tilt(a)
    except ValueError as e: 
        print(e)
        time.sleep(2)
