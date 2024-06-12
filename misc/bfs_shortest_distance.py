'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. 

You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.

Each 1 marks a building which you cannot pass through.

Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0),(0,4),(2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:

There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

'''

from collections import deque

def get_shortest_distance(grid):
    m, n = len(grid), len(grid[0])

    starts = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                starts += [ (i, j) ]
    buildings = len(starts)

    distances = [ [0 for j in range(n) ] for i in range(m) ]
    reach = [ [0 for j in range(n) ] for i in range(m) ]
    
    def dfs(grid, start, reach, distances):
        visited = [ [ False for j in range(n) ] for i in range(m) ]
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0]]
        
        level = 0
        dq = deque([ start ])
        while dq:
            k = 0
            l = len(dq)
            print(dq)
            while k < l:
                (i, j) = dq.popleft()
                k += 1
                if visited[i][j]:
                    continue

                reach[i][j] += 1
                visited[i][j] = True
                distances[i][j] += level

                for di, dj in directions:                
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and not visited[ni][nj]:
                        dq.append((ni, nj))

            level += 1
        print(distances)

    for start in starts:
        print(start)
        dfs(grid, start, reach, distances)
    
    min_distance = m + n
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and reach[i][j] == buildings:
                min_distance = min(min_distance, distances[i][j])

    return min_distance

grid = [ [1, 0, 2, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0] ]
print(get_shortest_distance(grid))