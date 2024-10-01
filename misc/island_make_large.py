'''
finding the largest possible island in a binary matrix after changing at most one 0 to 1. An island is defined as a group of 1s connected 4-directionally (up, down, left, right).
'''


def largest_island(grid):
    n = len(grid)
    if n == 0:
        return 0

    def dfs(x, y, index):
        stack = [(x, y)]
        area = 0
        while stack:
            i, j = stack.pop()
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = index
                area += 1
                stack.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
        return area

    index = 2
    area_map = {}
    max_area = 0

    # First pass: mark each island with a unique index and calculate its area
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                area = dfs(i, j, index)
                area_map[index] = area
                max_area = max(max_area, area)
                index += 1

    # Second pass: check each 0 cell to see the potential island size if changed to 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                seen = set()
                potential_area = 1
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                        index = grid[x][y]
                        if index not in seen:
                            seen.add(index)
                            potential_area += area_map[index]
                max_area = max(max_area, potential_area)

    return max_area

# Example usage
grid = [
    [1, 0],
    [0, 1]
]
print(largest_island(grid))  # Output: 3
