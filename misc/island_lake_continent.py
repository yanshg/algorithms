
class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [ 1 ] * n
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

    def get_size(self, x):
        rootx = self.find(x)
        return self.sizes[rootx]

    def get_count(self):
        return self.count


class Solution:
    def __init__(self, matrix):
        self.matrix = [ row[:] for row in matrix ]
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.init_uf()


    def init_uf(self):
        rows = self.rows
        cols = self.cols
        self.ocean = (rows, 0)

        self.uf = UF(rows * cols + 1)
        for i in range(rows):
            for j in range(cols):
                # union ocean points
                if self.matrix[i][j] == '0' and \
                   (i==0 or i==rows-1 or j==0 or j==cols-1):
                    self.union((i, j), self.ocean) 

                # union neighbor top and left points
                if i>0 and self.matrix[i][j] == self.matrix[i-1][j]:
                    self.union((i, j), (i-1, j))
                if j>0 and self.matrix[i][j] == self.matrix[i][j-1]:
                    self.union((i, j), (i, j-1))

    def union(self, p1, p2):
        (r1, c1) = p1
        (r2, c2) = p2
        self.uf.union(r1 * self.cols + c1, r2 * self.cols + c2)

    def is_ocean(self, p):
        (r, c) = p
        return self.uf.connected(r * self.cols + c, self.rows * self.cols)

    def is_lake(self, p):
        (r, c) = p
        return self.matrix[r][c]=='0' and not self.is_ocean(p)

    def get_size(self, p):
        (r, c) = p
        return self.uf.get_size(r * self.cols + c)

    def get_largest_lake_continent_area(self):
        max_lake_area = float('-inf')
        max_continent_area = float('-inf')
        max_r = -1
        max_c = -1

        for i in range(self.rows):
            for j in range(self.cols):
                if self.is_lake((i, j)):
                    area = self.get_size((i, j))
                    if area > max_lake_area:
                        max_lake_area = area
                        max_r = i
                        max_c = j

        # get the continent which contain the lake with max area
        if max_r != -1:
            # found a lake
            j = max_c
            while j >= 0 and self.matrix[max_r][j] == '0':
                j -= 1
            max_continent_area = self.get_size((max_r, j)) 

        return max_lake_area+max_continent_area if max_lake_area != float('-inf') else -1


matrix=[
    ['0','0','0','0','0','0','0'],
    ['0','0','1','1','1','0','0'],
    ['0','0','1','0','1','0','0'],
    ['0','0','1','1','1','0','0'],
    ['0','0','0','0','0','0','0'],
    ['1','1','1','1','1','1','0'],
    ['0','0','0','0','0','1','0'],
]

solution=Solution(matrix)
print(solution.get_largest_lake_continent_area())

