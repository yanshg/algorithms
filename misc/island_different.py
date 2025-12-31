def get_different_islands(matrix):

    islands = set()
    rows = len(matrix)
    cols = len(matrix[0])

    # s: start
    # u: up
    # d: down
    # l: left
    # r: right
    def dfs(matrix, i, j, directions = [], direction = 's'):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0:
            return
        
        matrix[i][j] = 0
        directions += [ direction ]
        dfs(matrix, i+1, j, directions, 'd')
        dfs(matrix, i, j+1, directions, 'r')
        dfs(matrix, i-1, j, directions, 'u')
        dfs(matrix, i, j-1, directions, 'l')
        #directions += [ "-" + direction ]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                directions = []
                dfs(matrix, i, j, directions, 's')
                islands.add(''.join(directions))

    print(islands)
    return len(islands)


matrix = [[0., 0, 0, 0., 0., 1, 1, 1, 0.],
          [0., 1, 1, 0., 0., 1, 1, 1, 0.],
          [0., 1, 1, 0., 0., 1, 1, 1, 0.],
          [0., 0., 0, 0, 0., 0., 0, 0, 0.],
          [0., 0., 1, 1, 0., 0., 1, 1, 0.],
          [0., 0., 1, 0, 0., 0., 1, 1, 0.],
          [0., 0., 0., 1, 1, 1, 0., 0., 0.],
          [0., 0., 0., 1, 1, 1, 0., 0., 0.],
          [0., 0., 0., 1, 1, 1, 0., 0., 0.]]

assert get_different_islands(matrix) == 3

matrix= [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]]

assert get_different_islands(matrix) == 1

matrix = [[1,1,0,1,1],
          [1,0,0,0,0],
          [0,0,0,0,1],
          [1,1,0,1,1]]

assert get_different_islands(matrix) == 3

