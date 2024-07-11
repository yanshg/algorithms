'''
You are given a 2D char matrix representing the game board.'M' represents an unrevealed mine,'E' represents an unrevealed empty square,'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.

If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent

unrevealed squares should be revealed recursively.

If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.

Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]


Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

 Explanation:
Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]


Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]


Explanation:
'''

def minesweeper(board, click):
    m, n = len(board), len(board[0])
    directions = [ [ 0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    def is_valid(r, c):
        if 0 <= r < m and 0 <= c < n:
            return True
        return False
    
    def get_mine_num(board, r, c):
        mine_num = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and board[nr][nc] == 'M':
                mine_num += 1
        return mine_num
            
    # dfs to re-set all cells which minimum is 0
    def dfs(board, r, c, visited):
        if not is_valid(r, c) or board[r][c] != 'E' or (r, c) in visited:
            return
        
        visited.add((r, c))
        mine_num = get_mine_num(board, r, c)
        if mine_num == 0:
            board[r][c] = 'B'
            for dr, dc in directions:
                dfs(board, r + dr, c + dc, visited)
        else:
            board[r][c] = str(mine_num)

    r, c = click
    if is_valid(r, c):
        if board[r][c] == 'M':
            board[r][c] = 'X'
        elif board[r][c] == 'E':
            dfs(board, r, c, set())

    return board

board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
click = [3,0]
print(minesweeper(board, click))
