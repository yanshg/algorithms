'''
Count different palindromic subsequences
'''

# DP[i][j]: means different palindromic subsequences of s[i:j+1]

def get_different_palindromic_subsequences(s):
    n = len(s)
    DP = [ [ {""} for j in range(n) ] for i in range(n) ]

    for i in range(n):
        for j in range(n):
            print(i, j, DP[i][j], len(DP[i][j]))

    for i in reversed(range(n)):
        for j in range(i, n):
            if i == j:
                DP[i][j].add(s[i])
            else:
                # include all sets of sub strings (s[i:j] and s[i+1:j+1])
                if s[i] == s[j]:
                    for p in DP[i+1][j-1]:
                        DP[i][j].add(s[i]+p+s[j])
                        
                DP[i][j] |= DP[i+1][j]
                DP[i][j] |= DP[i][j-1]
            #print(i, j, DP[i][j])

    for i in range(n):
        for j in range(n):
            print(i, j, DP[i][j])  

    print(DP[0][-1])

    # exclude the ''
    return len(DP[0][-1]) - 1

s = 'a'
print(get_different_palindromic_subsequences(s))

s = "aba"
print(get_different_palindromic_subsequences(s))


s = "abcac"
print(get_different_palindromic_subsequences(s))

s = "aaa"
print(get_different_palindromic_subsequences(s))

            