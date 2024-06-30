'''
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]

Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
'''

def get_longest_consecutive_ones(grid):
    m, n = len(grid), len(grid[0])

    # DP[i][j][0]: longest line of consecutive one for horizontal at (i, j)
    # DP[i][j][1]: longest line of consecutive one for vertical at (i, j)
    # DP[i][j][2]: longest line of consecutive one for diagonal at (i, j)
    # DP[i][j][3]: longest line of consecutive one for anti-diagonal at (i, j)
    
    DP = [ [ [ 0, 0, 0, 0 ] for j in range(n) ] for i in range(m) ]
    for i in range(m):
        for j in range(n):
            for k in range(4):
                DP[i][j][k] = 1 if grid[i][j] else 0

    res = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if j > 0:
                    DP[i][j][0] += DP[i][j-1][0]
            
                if i > 0:
                    DP[i][j][1] += DP[i-1][j][1]
            
                if i > 0 and j > 0:
                    DP[i][j][2] += DP[i-1][j-1][2]

                if i > 0 and j < n-1:
                    DP[i][j][3] += DP[i-1][j+1][3]

            res = max(res, DP[i][j][0], DP[i][j][1], DP[i][j][2], DP[i][j][3])

    return res

grid = [[0,1,1,0],
        [0,1,1,0],
        [1,0,0,0]]
print(get_longest_consecutive_ones(grid))
