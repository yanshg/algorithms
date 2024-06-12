# longest palindrome subsequence between string s and t

def longest_palindrome_subsequence_length(s: str) -> int:
    if not s:
        return 0
    
    n = len(s)

    DP = [ [ 0 for j in range(n) ] for i in range(n) ]
    for i in reversed(range(n)):
        for j in range(i, n):
            if i == j:
                DP[i][j] = 1
            elif s[i] == s[j]:
                DP[i][j] = DP[i+1][j-1] + 2
            else:
                DP[i][j] = max(DP[i][j-1], DP[i+1][j])
    print(DP)
    return DP[0][-1]


def longest_palindrome_subsequence(s: str) -> int:
    if not s:
        return ''
    
    n = len(s)

    DP = [ [ '' for j in range(n) ] for i in range(n) ]
    for i in reversed(range(n)):
        for j in range(i, n):
            if i == j:
                DP[i][j] = s[i]
            elif s[i] == s[j]:
                DP[i][j] = s[i] + DP[i+1][j-1] + s[j]
            else:
                DP[i][j] = DP[i][j-1]
                if len(DP[i][j]) < len(DP[i+1][j]):
                    DP[i][j] = DP[i+1][j]

    print(DP)
    return DP[0][-1]

s = 'etihabhidfe'
print(longest_palindrome_subsequence_length(s))
print(longest_palindrome_subsequence(s))
