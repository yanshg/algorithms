'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate,count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand (0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand (0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand (1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand (2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

'''

class UF:
    def __init__(self, n):
        self.parent = [ n ] * n
        self.size = [ 0 ] * n
        self.capacity = n
        self.count = 0

    # 
    def add(self, p):
        assert p >= 0 and p < self.capacity

        if self.size[p] != 0:
            return
        
        self.parent[p] = p
        self.size[p] = 1
        self.count += 1

    def find(self, p):
        assert p >= 0 and p < self.capacity

        if self.size[p] == 0:
            return None
        
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)

        if rootp is None or rootq is None or rootp == rootq:
            return
        
        if self.size[rootp] > self.size[rootq]:
            rootp, rootq = rootq, rootp

        self.parent[rootp] = rootq
        self.size[rootq] += self.size[rootp]

        self.count -= 1

    def get_count(self):
        return self.count

class Matrix:
    def __init__(self, m, n):
        self.matrix = [ [ 0 for j in range(n) ]  for i in range(m) ]
        self.uf = UF(m * n)
        self.rows = m
        self.cols = n

    def is_valid(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols
    
    def add(self, i, j):
        if self.is_valid(i, j):
            self.matrix[i][j] = 1
            index = i * self.cols + j
            self.uf.add(index)

            for di,dj in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
                ni, nj = i + di, j + dj
                if self.is_valid(ni, nj) and \
                    self.matrix[ni][nj] == 1:
                    nindex = ni * self.cols + nj
                    self.uf.union(index,  nindex)

        return self.uf.get_count()


m, n = 3, 3
positions = [[0,0], [0,1], [1,2], [2,1]]

matrix = Matrix(m, n)
result = [ matrix.add(pi, pj) for pi, pj in positions ]
print(result)

            
