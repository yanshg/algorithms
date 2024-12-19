"""
Generate a minesweeper grid (2x3) with 3 randomly-placed mines 
"""

import random

def generate_random_minesweeper(rows, cols, mines):
    matrix = [ [ '.' for j in range(cols) ] for i in range(rows) ]

    positions = random.sample(range(rows * cols), mines)

    for position in positions:
        row, col = position // cols, position % cols
        matrix[row][col] = 'X'

    return matrix

print(generate_random_minesweeper(6, 7, 3))