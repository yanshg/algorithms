"""
  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
"""

from collections import deque

def pacific_atlantic(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    top = [ (0, i) for i in range(cols) ]
    left = [ (i, 0) for i in range(rows) ]
    right = [ (i, cols-1) for i in range(rows) ]
    bottom = [ (rows-1, i) for i in range(cols) ]

    pacific = set( top + left )
    atlantic = set( right + bottom )

    def bfs(vset):
        dq = deque(list(vset))
        while dq:
            r,c = dq.popleft()
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and \
                    (nr,nc) not in vset and \
                    matrix[nr][nc] >= matrix[r][c]:
                    dq.append((nr,nc))
                    vset.add((nr,nc))
        return vset

    bfs(pacific)
    bfs(atlantic)
    return sorted(list(pacific & atlantic))

matrix = [
       [ 1, 2, 2, 3, 5 ],
       [ 3, 2, 3, 4, 4 ],
       [ 2, 4, 5, 3, 1 ],
       [ 6, 7, 1, 4, 5 ],
       [ 5, 1, 1, 2, 4 ]
]

assert pacific_atlantic(matrix) == [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
