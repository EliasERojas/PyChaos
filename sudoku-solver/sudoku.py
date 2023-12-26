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

def board_valid (board : list[list[int]]) :
    for i in range(0,SIZE) :
        if not row_valid(board,i) :
            return False
        for j in range (0,SIZE) :
            if not col_valid(board, j) :
                return False
            if j % 3 == 0 and i % 3 == 0 and not box_valid(board,i,j):
                return False
    return True

def row_valid (board : list[list[int]], row : int) :
    in_row = [EMPTY] * 10
    for i in range (0,SIZE) : 
        cell_value = board[row][i]
        if cell_value != EMPTY and in_row[cell_value] :
            return False
        in_row[cell_value] = FILLED
    return True
            
def col_valid (board : list[list[int]], col : int) :
    in_col = [EMPTY] * 10
    for i in range (0,SIZE) : 
        cell_value = board[i][col]
        if cell_value != EMPTY and in_col[cell_value] :
            return False
        in_col[cell_value] = FILLED
    return True

def box_valid (board : list[list[int]], offset_x : int, offset_y : int) :
    in_box = [EMPTY] * 10
    for i in range (0,3) :
        for j in range (0,3) :
            cell_value = board[offset_x + i][offset_y + j]
            if cell_value != EMPTY and in_box[cell_value] :
                return False
            in_box[cell_value] = FILLED
    return True

def get_empty_cells (board : list[list[int]]) :
    res = []
    for i in range(0,SIZE) : 
        for j in range(0,SIZE) : 
            if board[i][j] == EMPTY :
                res.append((i,j))
    return res

def solve_sudoku (board : list[list[int]], position_list : list) :
    if not board_valid(board) : 
        return

    if not position_list :
        print(board)
        return

    next_pos = position_list.pop()
    x = next_pos[0]
    y = next_pos[1]

    for i in range (0,SIZE) :
        board[x][y] = i + 1
        solve_sudoku(board, position_list)
        board[x][y] = EMPTY

    position_list.append(next_pos)

a = get_empty_cells(sudoku_puzzle)
solve_sudoku(sudoku_puzzle, a)
