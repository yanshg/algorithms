class Solution(object):
    def longestIncreasingPath(self, matrix):
        def dfs(matrix, rows, cols, lookup, r, c):
            print("dfs: ",r, c)
            if lookup[r][c] == -1:
                max_len = 1
                for dr,dc in [(0,-1), (0,1), (-1,0), (1,0)]:
                    nr,nc = r+dr,c+dc
                    if (0<=nr<rows and 0<=nc<cols) and \
                        matrix[nr][nc] > matrix[r][c]:
                        max_len = max(max_len, 1 + dfs(matrix, rows, cols, lookup, nr, nc))
                lookup[r][c] = max_len
            print("dfs: ",r, c)
            return lookup[r][c]

        rows,cols = len(matrix), len(matrix[0])
        max_len = 1
        lookup = [ [ -1 for c in range(cols) ] for r in range(rows) ]
        print(str(lookup))
        for r in range(rows):
            for c in range(cols):
                if lookup[r][c] == -1:
                    dfs(matrix, rows, cols, lookup, r, c)
                    max_len = max(max_len, lookup[r][c])
                print(str(lookup))
        return max_len

matrix = [[3,4,5],[3,2,6],[2,2,1]]
solution = Solution()
print(solution.longestIncreasingPath(matrix))
