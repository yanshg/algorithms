'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character'.'.

You may assume that there will be only one unique solution.
'''

def solve_sudoku(board):
    rows, cols = len(board), len(board[0])

    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[3 * (row // 3) + i // 3 ][ 3 * (col // 3) + i % 3 ] == num:
                return False
        return True
        
    def backtrack(board, row = 0, col = 0):
        if row == rows:
            print(board)
            return True
        
        if col == cols:
            return backtrack(board, row + 1, 0)

        if board[row][col] != '.':
            return backtrack(board, row, col + 1)

        # board[row][col] == '.'
        for c in '123456789':
            if is_valid(board, row, col, c):
                board[row][col] = c
                if backtrack(board, row, col + 1):
                    return True
                board[row][col] = '.'
        
        return False
    
    return backtrack(board, 0, 0)
    
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