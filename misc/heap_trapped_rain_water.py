'''
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Copy
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map before the rain.

After the rain, water are trapped between the blocks. The total volume of water trapped is 4.


从外头开始水漫金山， 使用 min heap, process with height by height

'''

import heapq

def get_trapped_water(grid):
    m, n = len(grid), len(grid[0])

    hq = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(hq, (grid[i][j], i, j))

    visited = [ [ False for j in range(n) ] for i in range(m) ]
    directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

    res = 0
    max_height = 0
    while hq:
        h, i, j = heapq.heappop(hq)
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        max_height = max(max_height, h)
        res += max_height - h
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                heapq.heappush(hq, (grid[ni][nj], ni, nj))

    return res

grid = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
print(get_trapped_water(grid))
    


