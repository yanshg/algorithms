'''

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

 

Example 1:

Input: 

    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]]

Output: 1

Example 2:

Input: 
    grid = [[1,1,0,1,1],
            [1,0,0,0,0],
            [0,0,0,0,1],
            [1,1,0,1,1]]
Output: 3

'''


class Solution:

    def __init__(self, matrix):
        self.matrix = [ item.copy() for item in matrix ]
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    # serialize the island as string
    def get_serialize_string_dfs(self, i, j, directions=[], direction='0'):
        matrix = self.matrix
        rows = self.rows
        cols = self.cols

        if i<0 or i>=rows or j<0 or j>=cols or matrix[i][j] == 0:
            return

        # change to water
        matrix[i][j] = 0

        # enter [i, j], pre order position
        directions += [direction]

        # up
        self.get_serialize_string_dfs(i-1,j, directions, '1')
        # down
        self.get_serialize_string_dfs(i+1,j, directions, '2')
        # left
        self.get_serialize_string_dfs(i,j-1, directions, '3')
        # right
        self.get_serialize_string_dfs(i,j+1, directions, '4')

        # leave [i, j], post order position
        directions += [ '-' + direction ]
        
    def get_distinct_islands(self):
        matrix = self.matrix
        rows = self.rows
        cols = self.cols

        islands = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # need use array to pass pointer as argument
                    directions = [] 
                    self.get_serialize_string_dfs(i,j,directions)
                    str = ''.join(directions)
                    islands.add(str)
                    #print(str)

        return len(islands)


matrix= [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]]

solution = Solution(matrix)
assert solution.get_distinct_islands() == 1

matrix = [[1,1,0,1,1],
          [1,0,0,0,0],
          [0,0,0,0,1],
          [1,1,0,1,1]]

solution = Solution(matrix)
assert solution.get_distinct_islands() == 3

