'''
Given amxngrid filled with non-negative numbers, find a path from top left to bottom right whichminimizesthe sum of all numbers along its path.

Note:You can only move either down or right at any point in time.

Example 1:

Copy
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
'''

def get_minimum_sum_path(grid):
    m, n = len(grid), len(grid[0])

    DP = [ [ 0 for j in range(n) ] for i in range(m) ]
    for i in range(m):
        for j in range(n):
            DP[i][j] = grid[i][j]
            if i == 0 and j > 0:
                DP[i][j] += DP[i][j-1]
            elif i > 0 and j == 0:
                DP[i][j] += DP[i-1][j]
            elif i > 0 and j > 0:
                DP[i][j] += min(DP[i-1][j], DP[i][j-1])

    print(DP)
    return DP[-1][-1]

grid = [[1,3,1],
 [1,5,1],
 [4,2,1]]

assert get_minimum_sum_path(grid) == 7
