'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.

'''

def get_maximal_square(grid):
    # DP[i][j]: means the long edge end with [i, j]

    # if grid[i][j] == 1:
    #    DP[i][j] = 1 + min( DP[i-1][j-1]. DP[i-1][j], DP[i][j-1] )
    #
    # base cases:
    #    DP[0][j] = grid[0][j] for j in range(n)
    #    DP[i][0] = grid[i][0] for i in range(m)

    max_edge = 0

    m, n = len(grid), len(grid[0])
    DP = [ [ 0 for j in range(n) ] for i in range(m) ]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                DP[i][j] = grid[i][j]
            elif grid[i][j] == 1:
                DP[i][j] = 1 + min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])
            
            max_edge = max(max_edge, DP[i][j])
    
    print(DP)
    return max_edge * max_edge

grid = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print(get_maximal_square(grid))