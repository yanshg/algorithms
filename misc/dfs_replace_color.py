'''
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B
'''

def replace_color(matrix, start, new_color):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])

    sr, sc = start
    old_color = matrix[sr][sc]
    visited = set()

    def dfs(matrix, point, old_color, new_color, visited):
        r, c = point
        if r < 0 or r >= rows or c < 0 or c >= cols or \
            matrix[r][c] != old_color or \
            point in visited:
            return
        
        visited.add((r, c))
        matrix[r][c] = new_color

        for dr, dc in [ (1, 0), (-1, 0), (0, 1), (0, -1) ]:
            dfs(matrix, (r + dr, c + dc), old_color, new_color, visited)

    dfs(matrix, start, old_color, new_color, visited)
    print(matrix)


matrix = [
    [ 'B', 'B', 'W' ],
    [ 'W', 'W', 'W' ],
    [ 'W', 'W', 'W' ],
    [ 'B', 'B', 'B' ]
]
replace_color(matrix, (2, 2), 'G')