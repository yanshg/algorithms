'''
Given a strings, partitions such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, givens="aab",

Return
[
  ["aa","b"],
  ["a","a","b"]
]
'''

def get_palindrome_partitions(s):
    l = len(s)

    def get_palindrome_state(s):
        isPalindrome = [ [ False for j in range(l) ] for i in range(l) ]

        for i in reversed(range(l)):
            for j in range(i, l):
                if i == j :
                    isPalindrome[i][j] = True
                elif s[i] == s[j]:
                    isPalindrome[i][j] = True if j == i+1 else isPalindrome[i+1][j-1]

        return isPalindrome
    
    def backtrack(s, isPalindrome, start, path = [], res = []):
        if start == l:
            res += [ path[:] ]
            return
        
        for i in range(start, l):
            if isPalindrome[start][i]:
                path.append(s[start:i+1])
                backtrack(s, isPalindrome, i+1, path, res)
                path.pop()

    # use memo to improve performance to O(n^2)
    def dfs_with_memo(s, isPalindrome, start, memo = {}):
        if start == l:
            return [[]]
        
        if start in memo:
            return memo[start]
        
        res = []
        for i in range(start, l):
            if isPalindrome[start][i]:
                res += [ [s[start:i+1]] + items for items in dfs_with_memo(s, isPalindrome, i+1, memo) ]
        memo[start] = res
        return res
    
    res = []
    memo = {}
    isPalindrome = get_palindrome_state(s)
    print(isPalindrome)

    #result = dfs_with_memo(s, isPalindrome, 0, {})
    #return result

    backtrack(s, isPalindrome, 0, [], res)
    return res

print(get_palindrome_partitions('aabb'))