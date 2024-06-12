'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        DP = [0] * l
        res = 0
        
        for i in range(1,l):
            if s[i] == ')':
                if s[i-1] == '(':
                    DP[i] = 2 + (DP[i-2] if i>=2 else 0)
                elif s[i-1] == ')':
                    last = i - DP[i-1] - 1
                    if last >= 0 and s[last] == '(':
                        DP[i] = 2 + DP[i-1] + (DP[last-1] if last>=1 else 0)
            res = max(res, DP[i])
            
        return res     

solution = Solution()
assert solution.longestValidParentheses(")()())") == 4
