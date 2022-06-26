
class Solution1:
    def __init__(self, matrix):
        self.matrix = [ item.copy() for item in matrix ]

    def max_island_area(self):
        matrix = self.matrix
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '0' and (i==0 or i==rows-1 or j==0 or j==cols-1):
                    self.sink_open_water_dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '0':
                    matrix[i][j] = '1'

        return max([ self.get_island_area_dfs(i,j) for i in range(rows) for j in range(cols) if matrix[i][j]=='1' ])


    def sink_open_water_dfs(self, i, j):
        matrix = self.matrix
        rows = len(matrix)
        cols = len(matrix[0])
        if i<0 or i>=rows or j<0 or j>=cols or matrix[i][j] == '-1':
            return

        if matrix[i][j] == '0':
            matrix[i][j] = '-1'
            self.sink_open_water_dfs(i-1, j)
            self.sink_open_water_dfs(i+1, j)
            self.sink_open_water_dfs(i, j-1)
            self.sink_open_water_dfs(i, j+1)

    def get_island_area_dfs(self, i, j):
        matrix = self.matrix
        rows = len(matrix)
        cols = len(matrix[0])
        if i<0 or i>=rows or j<0 or j>=cols or matrix[i][j] != '1':
            return 0

        matrix[i][j] = '0'
        return 1 + self.get_island_area_dfs(i-1,j) + \
                   self.get_island_area_dfs(i+1,j) + \
                   self.get_island_area_dfs(i,j-1) + \
                   self.get_island_area_dfs(i,j+1)


class UF:
    def __init__(self, n):
        self.sizes = [1] * n
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
        self.count = n

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return

        if self.sizes[rootp] > self.sizes[rootq]:
            rootp, rootq = rootq, rootp

        self.parents[rootp] = rootq
        self.sizes[rootq] += self.sizes[rootp]
        self.count -= 1

    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq

    def count(self):
        return self.count

    def size(self, p):
        rootp = self.find(p)
        return self.sizes[rootp]

class Solution2:
    def __init__(self, matrix):
        self.matrix = matrix
        self.init_uf(matrix)

    def init_uf(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        uf = UF(rows * cols + 1)
        dummy = rows * cols

        for i in range(rows):
            for j in range(cols):
                # connect open water to dummy node
                if matrix[i][j] == '0' and (i==0 or i==rows-1 or j==0 or j==cols-1):
                    uf.union(i*rows + j, dummy)
                # connect nodes with same value of neighbors (left and up)
                if i>0 and matrix[i-1][j] == matrix[i][j]:
                    uf.union((i-1)*cols + j, i*cols+j)
                if j>0 and matrix[i][j-1] == matrix[i][j]:
                    uf.union(i*cols + j - 1, i*cols+j)

        for i in range(1,rows-1):
            for j in range(1,cols-1):
                # connect inner water
                if matrix[i][j] == '0' and (not uf.connected(i*cols+j, dummy)):
                    uf.union(i*cols+j, i*cols+j-1)

        self.rows = rows
        self.cols = cols
        self.uf = uf
        self.dummy = dummy

    def num_islands(self):
        return self.uf.count()

    def max_island_area(self):
        rows = self.rows
        cols = self.cols
        return max([ self.uf.size(i*cols+j) for i in range(rows) for j in range(cols) if self.matrix[i][j]=='1' ])

matrix=[
    ['0','0','0','0','0','0','0'],
    ['0','0','1','1','1','0','0'],
    ['0','0','1','0','1','0','0'],
    ['0','0','1','1','1','0','0'],
    ['0','0','0','0','0','0','0'],
    ['1','1','1','1','1','1','0'],
    ['0','0','0','0','0','1','0'],
]

new_matrix = matrix.copy()

solution1=Solution1(matrix)
print(solution1.max_island_area())

solution2=Solution2(new_matrix)
print(solution2.max_island_area())

