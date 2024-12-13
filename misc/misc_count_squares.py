'''
To design a function that takes in a list of points and returns the number of squares that can be formed, we need to consider all possible combinations of four points and check if they form a square. Here's a step-by-step approach:

Generate Combinations: Use combinations from the itertools library to generate all possible groups of four points.
Check Valid Square: For each combination, check if the four points form a valid square using the distance-based method.
Count Valid Squares: Keep a count of all valid squares found.

'''

from itertools import combinations
from collections import defaultdict

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def is_valid_square(p1, p2, p3, p4):
    points = [p1, p2, p3, p4]
    distances = defaultdict(int)
    
    for i in range(len(points)-1):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            distances[d] += 1
    
    if len(distances) != 2:
        return False
    
    side, diagonal = sorted(distances.keys())
    
    return distances[side] == 4 and distances[diagonal] == 2 and side > 0 and diagonal == 2 * side

def count_squares(points):
    count = 0
    for comb in combinations(points, 4):
        print(comb)
        if is_valid_square(*comb):
            print("valid square")
            count += 1
    return count

# Example usage:
points = [[0, 0], [1, 1], [1, 0], [0, 1], [2, 2], [2, 0], [0, 2], [2, 1], [1, 2]]
print(count_squares(points))  # Output: 1