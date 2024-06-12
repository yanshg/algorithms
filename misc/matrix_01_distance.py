
def matrix01(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dist = [ [ float('inf') for j in range(cols) ] for i in range(rows) ]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                dist[i][j] = 0
            else:
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j]+1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1]+1)
    #print(dist)

    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if i < rows - 1:
                dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
            if j < cols - 1:
                dist[i][j] = min(dist[i][j], dist[i][j+1]+1)
    
    return dist

matrix = [[1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 1, 1, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1]]
print(matrix01(matrix))
