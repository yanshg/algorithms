'''

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:

Input:
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.

'''

# use A*

from heapq import heappush, heappop
from collections import defaultdict

# heap sort "steps + manhattan_distance" for every (y, x)
# when manhattan distance < k - used_eliminations, then get the result.

class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])

        if m + n - 2 <= k:
            return m + n - 2

        manhattan_distance = lambda y, x: m + n - y - x - 2
        neighborhood = lambda y, x: [
            (y, x) for y, x in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]
            if 0 <= y < m and 0 <= x < n
        ]

        fringe_heap = [(manhattan_distance(0, 0), 0, 0, 0, 0)]

        # min_eliminations is dict structure with { (y, x): k + 1 }
        # initially with { (0,0): 0 }
        min_eliminations = defaultdict(lambda: k + 1, {(0, 0): 0})

        while fringe_heap:
            print("fringe_heap: ", fringe_heap)
            print("min_eliminations: ", min_eliminations)
            estimation, steps, eliminations, y, x = heappop(fringe_heap)

            if estimation - steps <= k - eliminations:
                return estimation

            for y, x in neighborhood(y, x):
                print("eliminations: ", eliminations)
                print("y: ",y, "x: ", x)
                print("y,x: ", grid[y][x])
                next_eliminations = eliminations + grid[y][x]

                if next_eliminations < min_eliminations[(y, x)]:
                    heappush(fringe_heap, (steps + 1 + manhattan_distance(y, x), steps + 1, next_eliminations, y, x))
                    min_eliminations[(y, x)] = next_eliminations

        return -1

grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]]
print(grid[0][1])
k = 1

solution=Solution()
assert solution.shortestPath(grid,k) == 6
