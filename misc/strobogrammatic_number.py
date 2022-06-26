'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: n = 2
Output: ["11","69","88","96"]

Example 2:

Input: n = 1
Output: ["0","1","8"]
'''

# Recursion
class Solution(object):
    def findStrobogrammatic(self, n):
        def find(n,m):
            if n == 0:
                return [""]
            if n == 1:
                return ["0","1","8"]
            prev=find(n-2,m)
            ans = []
            for i in prev:
                if n < m:
                    ans.append("0" + i + "0")
                ans.append("1" + i + "1")
                ans.append("6" + i + "9")
                ans.append("9" + i + "6")
                ans.append("8" + i + "8")
            return ans
        return find(n,n)

solution=Solution()
res = solution.findStrobogrammatic(3)
print(res)
