'''
mincut(0, n) = 1 + min((mincut(0, 0) + mincut(1, n)),
                       (mincut(0, 1) + mincut(2, n)),
                       (mincut(0, 2) + mincut(3, n)),
                       ...
                       (mincut(0, n-1) + mincut(n, n)),

the longest Palindrome substring + remaining   should be minimal cut

From the left side:

mincut("aaabcd") = 1 + mincut("aaa") + mincut("bcd")

From the right side:

mincut("aaabcd") = 1 + mincut("aaabc") + mincut("d") =
                   1 + mincut("aaab") + 1 + mincut("c") + mincut("d") =
                   1 + mincut("aaa") + 1 + mincut("b") + 1 + mincut("c") + mincut("d") =
                   1 + mincut("aaa") + mincut("bcd")

So prove that the mincut is no matter the direction:  from left to right, or from right to left

'''



def palindrome_min_cut(s: str) -> int:
    if not s:
        return 0
    
    n = len(s)
    
    def get_palindrome_state(s):
        isPalin = [ [ False for j in range(n) ] for i in range(n) ]
        for i in reversed(range(n)):
            for j in range(i, n):
                if i == j:
                    isPalin[i][j] = True
                elif s[i] == s[j]:
                    isPalin[i][j] = True if j == i+1 else isPalin[i+1][j-1]
        return isPalin
    
    def get_palindrome_min_cut(s, isPalin, i, j, memo):
        if isPalin[i][j]:
            return 0
        
        if memo[i][j] == -1:
            res = j - i
            for k in range(i, j-1):
                res = min(res, 1 + get_palindrome_min_cut(s, isPalin, i, k, memo) +
                               get_palindrome_min_cut(s, isPalin, k+1, j, memo))
            memo[i][j] = res

        return memo[i][j]
    
    def get_palindrome_min_cut_optimized(s, isPalin):
        n = len(s)

        if isPalin[0][n-1]:
            return 0
        
        DP = [ n-1 ] * n
        for i in range(n):
            # Calcuate C[i] which do not depend on s[i+1:]
            if isPalin[0][i]:
                DP[i] = 0
            else:
                for j in range(1, i+1):
                    if isPalin[j][i]:
                        DP[i] = min(DP[i], 1 + DP[j-1])
        print(DP)
        return DP[-1]
    
    isPalin = get_palindrome_state(s)
    print(isPalin)

    #memo = [ [ -1 for j in range(n) ] for i in range(n) ]
    #return get_palindrome_min_cut(s, isPalin, 0, n-1, memo)
    return get_palindrome_min_cut_optimized(s, isPalin)

s = 'ihhihab'
print(palindrome_min_cut(s))



