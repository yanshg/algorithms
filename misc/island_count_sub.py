'''

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Input: 

grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]], 

grid2 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

Output: 3

Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:


Input: 
grid1 = [[1,0,1,0,1],
         [1,1,1,1,1],
         [0,0,0,0,0],
         [1,1,1,1,1],
         [1,0,1,0,1]], 

grid2 = [[0,0,0,0,0],
         [1,1,1,1,1],
         [0,1,0,1,0],
         [0,1,0,1,0],
         [1,0,0,0,1]]

Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.

'''


# sink the non-sub islands,  the remaining are sub islands
class Solution:

    def __init__(self):
        return

    def count_sub_islands(self, grid1, grid2):
        rows = len(grid2)
        cols = len(grid2[0])
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    # not sub island, sink it
                    self.sink_island(grid2, i, j)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    # sub island, sink it also
                    self.sink_island(grid2, i, j)
                    res += 1
        return res

    def sink_island(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        if i<0 or i >= rows or j<0 or j>=cols or grid[i][j] == 0:
            return

        # sink it
        grid[i][j] = 0

        # sink neighbors
        self.sink_island(grid, i+1, j)
        self.sink_island(grid, i-1, j)
        self.sink_island(grid, i, j+1)
        self.sink_island(grid, i, j-1)


grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]] 

grid2 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

solution = Solution()
assert solution.count_sub_islands(grid1, grid2) == 3

grid1 = [[1,0,1,0,1],
         [1,1,1,1,1],
         [0,0,0,0,0],
         [1,1,1,1,1],
         [1,0,1,0,1]] 

grid2 = [[0,0,0,0,0],
         [1,1,1,1,1],
         [0,1,0,1,0],
         [0,1,0,1,0],
         [1,0,0,0,1]]

solution = Solution()
assert solution.count_sub_islands(grid1, grid2) == 2

