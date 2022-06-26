from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = defaultdict(int)
        for c in t:
            counter[c] += 1
        chars = set(t)

        min_len = float('inf')
        min_left = -1
        left = 0
        for right,c in enumerate(s):
            print(c)
            if c not in chars:
                continue

            counter[c] -= 1
            print(counter)

            # if any char's counter < 0, then check if move left
            while left < right and (s[left] not in chars or counter[s[left]] < 0):
                if s[left] in chars:
                    counter[c] += 1
                left += 1

            print(counter)
            if all([ True if counter[c] <= 0 else False for c in counter ]):
                if min_len > right-left+1:
                    min_left = left
                    min_len = right-left+1
                    print("min_left", min_left, "len:", min_len, "string:", s[min_left:(min_left+min_len)])

        return "" if min_left==-1 else s[min_left:(min_left+min_len)]

solution = Solution()

s = "ADOBECODEBANC"
t = "ABC"
solution.minWindow(s,t)


s = "a"
t = "a"
solution.minWindow(s,t)

s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
solution.minWindow(s,t)
