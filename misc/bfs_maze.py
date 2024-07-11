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

    move_directions = {       
        'left': (0, -1),
        'right': (0, 1),
        'up': (-1, 0),
        'down': (1, 0),
    }

    def is_valid(matrix, point):
        i, j = point
        if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 0:
            return True
        return False
    
    def get_next_point(point, direction):
        if direction not in move_directions:
            return point
        
        i, j = point
        di, dj = move_directions[direction]
        return (i + di, j + dj)
    
    def get_neighbor_or_dest_point(matrix, start, dest):       
        res = []

        for direction in move_directions:    
            prev = None
            current = start
            get_to_dest = False
            while is_valid(matrix, current):
                if current == dest:
                    res += [ (direction, current) ]
                    get_to_dest = True
                    break
                prev = current
                current = get_next_point(current, direction)

            # if prev is start, means start's next point is not valid
            if not get_to_dest and prev and prev != start:
                res += [ (direction, prev) ]
        
        return res

    # bfs is better than dfs
    # dfs have some additional direction actions 
    def bfs(matrix, start, dest, res):
        visited = set()

        dq = deque([(start, [])])
        while dq:
            point, directions = dq.popleft()
            if point == dest:
                res += [ ' '.join(directions) ]
                return

            visited.add(point)
            for direction, neigh in get_neighbor_or_dest_point(matrix, point, dest):
                if neigh not in visited:
                    dq.append((neigh, directions + [direction]))        
        return

    def dfs(matrix, start, dest, directions, visited=set(), res=[]):
        if start == dest:
            res += [ ' '.join(directions) ]
            return       
        
        visited.add(start)
        for direction, neigh in get_neighbor_or_dest_point(matrix, start, dest):
            if neigh not in visited:
                directions.append(direction)
                dfs(matrix, neigh, dest, directions, visited, res)
                directions.pop()
        return

    res = []
    #dfs(matrix, start, dest, [], set(), res)
    bfs(matrix, start, dest, res)
    return res
        
matrix = [ [ 0, 0, 1, 0, 0 ],
           [ 0, 0, 0, 0, 0 ],
           [ 0, 0, 0, 1, 0 ],
           [ 1, 1, 0, 1, 1 ],
           [ 0, 0, 0, 0, 0 ] ]
print(maze(matrix, (0, 4), (4, 4)))

