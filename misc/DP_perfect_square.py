'''
Given a positive integer n, find the least number of perfect square numbers (for example,1, 4, 9, 16, ...) which sum to n.

For example, given n=12, return 3 because 12 = 4 + 4 + 4; given n=13, return 2 because 13 = 4 + 9.

'''


# f(n) = min (1 + f(n - i * i)) for i in [1, sqrt(n)]

# base cases: 
#    f(0) = 0
#    f(1) = 1

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