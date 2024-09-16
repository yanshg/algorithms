'''
DP: given an input and pattern solve a regex expression matching support for '.' and '*'

'''

# Recursion

# O(3 ^ m)    m = max (len(s), len(r))
def match_recursion(r: str, s: str) -> bool:
    # base cases:
    if not r:
        return not s
    
    if not s:
        return r == '*' * len(r)
    
    print("r: ", r, "s: ", s)
    # Recursion
    if r[0] in [ '.', s[0] ]:
        return match_recursion(r[1:], s[1:])
    elif r[0] == '*':
        return match_recursion(r[1:], s) or \
               match_recursion(r, s[1:])
    else:
        return False
    
# DP 
# r should be first argument

def match_dp(r: str, s: str) -> bool:
    #  r:    a.c*ef
    #  s:    abcdef

    # DP[i][j]: means match result for r[:i+1] and s[:j+1]
    #           default is False

    # DP[i]][j]:    DP[i-1][j-1]  if r[i] in [ '.', s[j]]
    #               DP[i-1][j] or DP[i][j-1] if r[i] == '*'
    #               False  otherwise

    # r' = '' + r
    # s' = '' + s
 
    # r'[i] = r[i-1]
    # s'[j] = s[j-1]

    # DP[0][0] = True
    #
    # DP[i]][j]:    DP[i-1][j-1]  if r[i-1] in [ '.', s[j-1]]
    #               DP[i-1][j] or DP[i][j-1] if r[i-1] == '*'
    #               False  otherwise

    m, n = len(r), len(s)
    DP = [ [ False for j in range(n+1) ] for i in range(m+1) ]
    print(DP)

    # base cases
    DP[0][0] = True
    for i in range(1, m+1):
        if r[i-1] == '*':
            DP[i][0] = DP[i-1][0]
    print(DP)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if r[i-1] in ['.', s[j-1]]:
                DP[i][j] = DP[i-1][j-1]
            elif r[i-1] == '*':
                DP[i][j] = DP[i-1][j] or DP[i][j-1]

    print(DP)
    return DP[-1][-1]

    
assert match_recursion(".bc", "abc")
assert match_recursion("a*bc", "abc")

assert match_dp(".bc", "abc")
assert match_dp("a*bc", "abc")
