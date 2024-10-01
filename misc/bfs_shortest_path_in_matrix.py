'''
finding the shortest path from the top-left corner to the bottom-right corner of an ( n \times n ) binary matrix. The path can only traverse cells containing 0 and can move in 8 possible directions (horizontally, vertically, and diagonally). If no such path exists, the function should return -1.
'''

from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    grid[0][0] = 1  # mark as visited

    while queue:
        row, col, path_length = queue.popleft()
        if row == n-1 and col == n-1:
            return path_length
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                queue.append((new_row, new_col, path_length + 1))
                grid[new_row][new_col] = 1  # mark as visited

    return -1

# Example usage
grid = [
    [0, 1],
    [1, 0]
]
print(shortest_path_binary_matrix(grid))  # Output: 2
