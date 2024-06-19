'''
On an N x N grid, each square grid[i][j] represents the elevation at that point(i,j).

Now rain starts to fall. At time t, the depth of the water everywhere ist. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square(0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Copy
Input: [[0,2],[1,3]]

Output:3

Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

Output: 16

Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.

grid[i][j] is a permutation of [0, ..., N*N - 1].

'''

import heapq

def swim_in_rising_water(grid):
    m, n = len(grid), len(grid[0])

    visited = [ [ False for j in range(n) ] for i in range(m) ]
    directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]

    max_height = 0
    hq = [ (grid[0][0], 0, 0) ]
    visited[0][0] = True

    while hq:
        h, i, j = heapq.heappop(hq)

        max_height = max(max_height, h)
        if i == m-1 and j == n-1:
            return max_height
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                heapq.heappush(hq, (grid[ni][nj], ni, nj))
                visited[ni][nj] = True

    return -1

grid = [[0,2],[1,3]]
print(swim_in_rising_water(grid))

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(swim_in_rising_water(grid))