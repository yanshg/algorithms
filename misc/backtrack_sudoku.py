'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character'.'.

You may assume that there will be only one unique solution.
'''

def solve_sudoku(board):
    m, n = len(board), len(board[0])

    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[3 * (row // 3) + i // 3 ][ 3 * (col // 3) + i % 3 ] == num:
                return False
        return True
        
    def backtrack(board):
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    print(i, j)
                    for c in '123456789':
                        if is_valid(board, i, j, c):
                            board[i][j] = c
                            if backtrack(board):
                                print(board)
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    return backtrack(board)
    
board = [
    ['7', '8', '.', '4', '.', '.', '1', '2', '.' ],
    ['6', '.', '.', '.', '7', '5', '.', '.', '9' ],
    ['.', '.', '.', '6', '.', '1', '.', '7', '8' ],
    ['.', '.', '7', '.', '4', '.', '2', '6', '.' ],
    ['.', '.', '1', '.', '5', '.', '9', '3', '.' ],
    ['9', '.', '4', '.', '6', '.', '.', '.', '5' ],
    ['.', '7', '.', '3', '.', '.', '.', '1', '2' ],
    ['1', '2', '.', '.', '.', '7', '4', '.', '.' ],
    ['.', '4', '9', '2', '.', '6', '.', '.', '7' ]
]
print(solve_sudoku(board))