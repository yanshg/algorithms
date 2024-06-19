'''
Given a strings, partitions such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, givens="aab",
Return

Copy
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

    res = []
    isPalindrome = get_palindrome_state(s)
    print(isPalindrome)
    backtrack(s, isPalindrome, 0, [], res)
    return res

print(get_palindrome_partitions('aab'))