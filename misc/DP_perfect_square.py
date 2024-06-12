'''
Given a positive integer n, find the least number of perfect square numbers (for example,1, 4, 9, 16, ...) which sum to n.

For example, given n=12, return 3 because 12 = 4 + 4 + 4; given n=13, return 2 because 13 = 4 + 9.

'''
import math

def get_perfect_square(n):
    if n <= 0:
        return 0
    
    DP = list(range(n+1))

    for i in range(2, n+1):
        for j in range(1, i):
            k = j * j
            if k > i:
                break
            DP[i] = min(DP[i], 1 + DP[i - k])
    
    print(DP)
    return DP[-1]

print(get_perfect_square(100))