'''
We have a grid of 1s and 0s; the 1s in a cell represent bricks. A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Copy
Example 1:
Input:

grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]

Output:
 [2]

Explanation: 

If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
Copy
Example 2:
Input:

grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]

Output:
 [0,0]

Explanation: 

When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.
Note:

The number of rows and columns in the grid will be in the range [1, 200].

The number of erasures will not exceed the area of the grid.

It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.

An erasure may refer to a location with no brick - if it does, no bricks drop.


思路: 这题题设是当brick通过hits数组打碎后，所有和第一行没有连在一起的brick就会掉落，问有多少brick会掉落。步骤如下:

(1) 我们可以用union find做。但union find只能连接不能断开，所以我们应该先处理hit brick之后的grid，找到所有connected component. 对于与第一行相连的component。我们用m * n这个特殊id表示和top连接的component, 因为按照row * n + col的方式定义union find的node id，m * n这个id是grid所有cell无法转换，非常适合做一个特殊id

(2) 找到hit之后的所有connected components后，我们倒过来把hit之后的brick加回去，每加一次的时候，查看和top连接的component的size，如果比之前的大，则有falling bricks，个数为newSize - size - 1,这里newSize是加上hit之后，与connected component的size，size是之前与top连接的component的size, 这里还要再减1是因为我们不算被hit的brick

'''

# Reverse thinking

# add back the hit brick into UF, and the increased count (connected to top) equal to the bricks falling.

class UF:
    def __init__(self, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])
        n = self.rows * self.cols + 1
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p):
        i, j = p
        k = i * self.cols + j
        while self.parent[k] != k:
            self.parent[k] = self.parent[self.parent[k]]
            k = self.parent[k]
        return k

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        
        if self.size[rootp] > self.size[rootq]:
            rootp, rootq = rootq, rootp

        self.size[rootq] += self.size[rootp]
        self.parent[rootp] = rootq
        self.count -= 1

    def get_count(self):
        return self.count

    def union_with_top(self, p):
        self.union(p, (self.rows, 0))

    def get_top_size(self):
        rootp = self.find((self.rows, 0))
        return self.size[rootp]

def connect_top_bricks(uf, grid):
    for i in range(uf.rows):
        for j in range(uf.cols):
            if grid[i][j] == 1:
                if i == 0:
                    uf.union_with_top((i, j))
                else:
                    if j > 0 and grid[i][j] == grid[i][j-1]:
                        uf.union((i, j), (i, j-1))
                    if grid[i][j] == grid[i-1][j]:
                        uf.union((i, j), (i-1, j))

def get_falling_bricks(grid, hits):
    if not grid:
        return []
    
    res = []

    uf = UF(grid)
    m, n = uf.rows, uf.cols

    for (hi, hj) in hits:
        if 0 <= hi < m and 0 <= hj < n:
            grid[hi][hj] = 2

    connect_top_bricks(uf, grid)
    
    for (hi, hj) in hits:
        if 0 <= hi < m and 0 <= hj < n:
            grid[hi][hj] = 1

            size1 = uf.get_top_size()
            connect_top_bricks(uf, grid)
            size2 = uf.get_top_size()
            if size2 > size1:
                res.append(size2 - size1 - 1)
            else:
                res.append(0)

            grid[hi][hj] = 0

    return res

grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
print(get_falling_bricks(grid, hits))

grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
print(get_falling_bricks(grid, hits))

