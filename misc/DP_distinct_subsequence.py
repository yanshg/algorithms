'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie,"ACE"is a subsequence of"ABCDE"while"AEC"is not).

Here is an example:
S="rabbbit", T="rabbit"

Retur 3
'''

def get_distinct_subsequence_count(s: str, t: str) -> int:
    
    # DP[i][j]: distinct subsequence count of s[:i+1] which equals to t[:j+1]

    # DP[i][j] = DP[i-1][j-1] + DP[i-1][j] if s[i] == t[j] else DP[i-1][j]

    # base cases:  DP[0][j] = 0  for 1<= j <= len(t)
    #              DP[i][0] = 1  for 0<= i <= len(s)


    m, n = len(s), len(t)

    # initialize DP
    DP = [ [ 0 for j in range(n+1) ] for i in range(m+1) ]
    for i in range(m+1):
        DP[i][0] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            DP[i][j] = DP[i-1][j]
            if s[i-1] == t[j-1]:
                DP[i][j] += DP[i-1][j-1]
                
    print(DP)
    return DP[-1][-1]

s="rabbbit"
t="rabbit"
assert get_distinct_subsequence_count(s, t) == 3
    
