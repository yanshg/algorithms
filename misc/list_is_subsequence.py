'''

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

 Example 1:

 Input: s = "abc", t = "ahbgdc"
 Output: true
 Example 2:

 Input: s = "axc", t = "ahbgdc"
 Output: false

'''

class Solution:

    @staticmethod
    def isSubsequence(s, t):
        i, j = 0, 0
        ls, lt = len(s), len(t)
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == ls


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        seen = 0
        for c in t:
            if s[seen] == c:
                seen += 1
            if seen == len(s):
                return True
        return False

# DP
# DP[i][j]:  True if s[:i+1] is sub sequence of t[:j+1] else False
#
# DP[i][j] = DP[i-1][j-1]  if s[i] == t[j]
# DP[i][j] = DP[i][j-1]    if s[i] != t[j]
#
# return DP[n][m]

class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls, lt = len(s)+1, len(t)+1
        DP = [ [ False for j in range(lt) ] for i in range(ls) ]
        for j in range(lt):
            DP[0][j] = True

        for i in range(1, ls):
            for j in range(1, lt):
                if s[i-1] == t[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = DP[i][j-1]
        return DP[-1][-1]
        
solution = Solution()
assert solution.isSubsequence('abc', 'ahbgdc')
assert not solution.isSubsequence('axc', 'ahbgdc')

solution = Solution2()
assert solution.isSubsequence('abc', 'ahbgdc')
assert not solution.isSubsequence('axc', 'ahbgdc')

solution = Solution3()
assert solution.isSubsequence('abc', 'ahbgdc')
assert not solution.isSubsequence('axc', 'ahbgdc')
