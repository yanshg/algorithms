def recursion(n, memo={}):
    if n == 0:
        return [ '' ]
    
    if n in memo:
        return memo[n]
    
    res = []
    for i in range(n):
        for left in recursion(i):
            for right in recursion(n-1-i):
                res += [ f"({left}){right}" ]

    memo[n] = res
    return res

def dp(n):
    DP = [ [] for i in range(n+1) ]
    
    DP[0] = [ '' ]
    for i in range(1, n+1):
        DP[i] = [ f"({left}){right}" \
                for j in range(i) \
                for left in DP[j] \
                for right in DP[i-1-j] ]
    
    return DP[n]

def generateParenthesis(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    result = []
    backtrack()
    return result


def dp_count(n):
    DP = [ 0 ] * (n+1)
    
    DP[0] = 1
    for i in range(1, n+1):
        for j in range(i):
           DP[i] += DP[j] * DP[i-1-j]
    return DP[n]

print(recursion(1))
print(recursion(2))
print(recursion(3))
print(recursion(4))
print(recursion(8))

print(dp(1))
print(dp(2))
print(dp(3))
print(dp(4))
print(dp_count(0))
print(dp_count(1))
print(dp_count(2))
print(dp_count(3))