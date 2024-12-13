'''
The "Image Smoother" problem on LeetCode involves applying a 3x3 filter to each cell of a grayscale image. The filter calculates the average of the cell and its surrounding eight cells, rounding down the result. If some surrounding cells are missing (e.g., at the edges or corners), only the existing cells are considered in the average.

Here's a brief overview of how the algorithm works:

Traverse Each Cell: Loop through each cell in the image.
Calculate Average: For each cell, compute the average of the cell and its valid surrounding cells.
Handle Boundaries: Ensure that cells at the edges and corners are handled correctly by only including valid neighbors in the average calculation.
Update Cell Value: Assign the rounded down average to the corresponding cell in the output image.

'''

def imageSmoother(M):
    m, n = len(M), len(M[0])
    res = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            count = 0
            total = 0
            for ni in (i-1, i, i+1):
                for nj in (j-1, j, j+1):
                    if 0 <= ni < m and 0 <= nj < n:
                        total += M[ni][nj]
                        count += 1
            res[i][j] = total // count
    
    return res