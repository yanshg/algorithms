'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

'''

def flip_surrounded_regions(board):
    rows, cols = len(board), len(board[0])
    visited = set()

    def sink_edge_dfs(board, r, c, visited):
        if r < 0 or r >= rows or c < 0 or c >= cols or \
            board[r][c] != 'O' or \
            (r, c) in visited:
            return
        
        board[r][c] = '#'
        visited.add((r, c))

        sink_edge_dfs(board, r-1, c, visited)
        sink_edge_dfs(board, r+1, c, visited)
        sink_edge_dfs(board, r, c-1, visited)
        sink_edge_dfs(board, r, c+1, visited)
        
    # Change all 'O's connected to edge to '#'
    for r in range(rows):
        sink_edge_dfs(board, r, 0, visited)
        sink_edge_dfs(board, r, cols - 1, visited)
        
    for c in range(cols):
        sink_edge_dfs(board, 0, c, visited)
        sink_edge_dfs(board, cols - 1, c, visited)

    # Change all remaining surrounded 'O's to 'X'
    # Change back all '#'s to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'
    
board = [
  ['X', 'X', 'X', 'X'],
  ['X', 'O', 'O', 'X'],
  ['X', 'X', 'O', 'X'],
  ['X', 'O', 'X', 'X']
]

print(board)
flip_surrounded_regions(board)
print(board)

        
    