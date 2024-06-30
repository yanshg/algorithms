'''
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100

The size of given string array won't exceed 600.

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation:
This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation:
You could form "10", but then you'd have nothing left. Better form "0" and "1".

'''

# Knapsack 0-1 problem

# DP[i][j][k]: mean max number of strings for strs[:i+1] with j 0s and k 1s.

# DP[i][j][k] = max(DP[i-1][j][k],            1 + DP[i-1][j - count(strs[i-1], '0')][k - count(strs[i-1], '1')])
#                   exclude strs[i]           include strs[i]

# base cases:
# STRs = [ '' ] + strs
# STRs[i] = strs[i-1]
# 
# DP[0][j][k] = 0
# DP[i][0][k] = 0
# DP[i][j][0] = 0

from collections import Counter

def get_max_number_strs(strs, m, n):
    if not strs or m == 0 or n == 0:
        return 0
    
    l = len(strs)
    DP = [ [ [0 for k in range(n + 1) ] for j in range(m + 1) ] for i in range(l + 1) ]

    for i in range(1, l+1):
        # Get counts for strs[i-1]
        counts = Counter(strs[i-1])
        c0, c1 = counts['0'], counts['1']

        for j in range(1, m + 1):
            for k in range(1, n + 1):                            
                DP[i][j][k] = DP[i-1][j][k]
                if j >= c0 and k >= c1:
                    DP[i][j][k] = max(DP[i][j][k], 1 + DP[i-1][j-c0][k-c1])

    print(DP)
    return DP[-1][-1][-1]

def get_max_number_strs_optimized(strs, m, n):
    if not strs or m == 0 or n == 0:
        return 0
    
    l = len(strs)
    DP = [ [0 for k in range(n + 1) ] for j in range(m + 1) ]

    for i in range(l):
        # Get counts for strs[i]
        counts = Counter(strs[i])
        c0, c1 = counts['0'], counts['1']

        for j in range(m, 0, -1):
            for k in range(n, 0, -1):                            
                if j >= c0 and k >= c1:
                    DP[j][k] = max(DP[j][k], 1 + DP[j-c0][k-c1])

    print(DP)
    return DP[-1][-1]

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(get_max_number_strs(strs, m, n))
print(get_max_number_strs_optimized(strs, m, n))