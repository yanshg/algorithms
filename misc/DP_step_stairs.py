'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

'''

# base cases:
# n = 0:  0
# n = 1:  1
# n = 2:  2
# n = 3:  3
# n = 4:  5

# DP[i] = DP[i-1] + DP[i-2]

def get_step_stair_ways(n):
    if n <= 3:
        return n
    
    DP = list(range(n+1))
    for i in range(4, n+1):
        DP[i] = DP[i-1] + DP[i-2]

    print(DP)
    return DP[-1]

print(get_step_stair_ways(100))

    




