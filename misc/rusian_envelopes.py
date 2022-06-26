

class Solution1:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        heights = list(map(lambda x: x[1], envelopes))
        
        # LIS 
        res = 1
        l = len(heights)
        DP = [1] * l
        for i in range(l):
            for j in range(i):
                if heights[i] > heights[j]:
                    DP[i] = max(DP[i], DP[j]+1)
                    res = max(res, DP[i])
        return res


class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # LIS
        def lis(nums):
            res = 1
            l = len(nums)
            DP = [1] * l
            for i in range(l):
                for j in range(i):
                    if nums[i] > nums[j]:
                        DP[i] = max(DP[i], DP[j]+1)
                        res = max(res, DP[i])
            return res
                        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return lis([ e[1] for e in envelopes ])


# patient sorting

# Imaging a Poke
# 2, 3, 4, 1   ===> 3
# 4, 3, 2, 5   ===> 2

# can only return the longest length.

import bisect
class Solution3:

    def maxEnvelopes(self, envelopes):

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        #envelopes.sort(key=cmp_to_key(lambda a,b: b[1] - a[1] if a[0] == b[0] else a[0] - b[0]))

        tops = []
        for w, h in envelopes:
            idx = bisect.bisect_left(tops, h)
            if idx == len(tops):
                tops += [ h ]
            else:
                tops[idx] = h
        return len(tops)


