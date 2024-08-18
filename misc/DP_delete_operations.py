'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

Input: "sea", "eat"
Output: 2

Explanation:
You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:

The length of given words won't exceed 500.
'''

# Solutions:
#    1. first get LCS, result = len(s) + len(t) - 2 * len(LCS)
#    2. directly using DP.

def get_delete_operations(s: str, t: str) -> int:
    # base cases:
    m, n = len(s), len(t)

    if not s or not t:
        return m + n
    
    # DP[i][j]: minimum deletions for s[:i+1] and t[:j+1]
    # Result: DP[m][n]
    DP = [ [ 0 for j in range(n+1) ] for i in range(m+1) ]
    for i in range(m+1):
        DP[i][0] = i
    for j in range(n+1):
        DP[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                DP[i][j] = DP[i-1][j-1]
            else:
                DP[i][j] = 1 + min(DP[i-1][j], DP[i][j-1])

    return DP[-1][-1]

s, t = "sea", "eat"
assert get_delete_operations(s, t) == 2