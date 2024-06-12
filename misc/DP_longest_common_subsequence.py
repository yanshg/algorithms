def longest_common_subsequence_length(s, t):
    if not s or not t:
        return 0
    
    # DP[i][j], LCS for s[:i+1] t[:j+1]
    m, n = len(s), len(t)

    DP = [ [ 0 for j in range(n+1)] for i in range(m+1) ]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    print(DP)
    return DP[m][n]

def longest_common_subsequence(s, t):
    if not s or not t:
        return ''
    
    # DP[i][j], LCS for s[:i+1] t[:j+1]
    m, n = len(s), len(t)

    DP = [ [ '' for j in range(n+1)] for i in range(m+1) ]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                DP[i][j] = DP[i-1][j-1] + s[i-1]
            else:
                DP[i][j] = DP[i-1][j]
                if len(DP[i][j]) < len(DP[i][j-1]):
                    DP[i][j] = DP[i][j-1]
    print(DP)
    return DP[m][n]

s = 'ayanusfhbegc'
t = 'byadnuskeh'
print(longest_common_subsequence_length(s, t))
print(longest_common_subsequence(s, t))

