'''

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up,down,left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Copy
Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

'''

from collections import deque

def maze(matrix, start, dest) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    move_directions = [      
        ('left',  (0, -1)),
        ('right', (0, 1)),
        ('up',    (-1, 0)),
        ('down',  (1, 0)),
    ]

    def is_valid(matrix, point):
        i, j = point
        if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 0:
            return True
        return False
      
    # bfs is better than dfs
    # dfs have some additional direction actions 
    def bfs(matrix, start, dest):
        if not is_valid(matrix, start):
            return
        
        visited = set()

        dq = deque([(start, [])])
        while dq:
            point, path = dq.popleft()
            if point == dest:
                return '->'.join(path)
            
            visited.add(point)
            for direction, (di, dj) in move_directions:
                ni, nj = point
                while is_valid(matrix, (ni + di, nj + dj)):
                    ni, nj = ni + di, nj + dj
                    if (ni, nj) == dest:
                        return '->'.join(path + [direction])

                if (ni, nj) != point and (ni, nj) not in visited:
                    dq.append(((ni, nj), path + [direction]))

        return ""

    return bfs(matrix, start, dest)
        
matrix = [ [ 0, 0, 1, 0, 0 ],
           [ 0, 0, 0, 0, 0 ],
           [ 0, 0, 0, 1, 0 ],
           [ 1, 1, 0, 1, 1 ],
           [ 0, 0, 0, 0, 0 ] ]
print(maze(matrix, (0, 4), (4, 4)))

