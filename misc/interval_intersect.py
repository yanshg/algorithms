'''

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 
Given two lists of closed intervals, each list of intervals is pairwise disjoint (non-overlapping) and in sorted order.
Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty, or can be
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.


'''


# Ask question:   1. close interval,  for [1,3], [3, 4],  intersection should be [3, 3],
#                 2. negative ?


class Solution:

    def get_intersections(self, intervals1, intervals2):
        res = []
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            s1, e1 = intervals1[i]
            s2, e2 = intervals2[j]
            lo = max(s1, s2)
            hi = min(e1, e2)

            if lo <= hi:
                res += [ [lo, hi] ]

            # move i or j according to the end points
            if e1 < e2:
                i += 1
            else:
                j += 1

        return res


solution = Solution()

A = [[0,2],[5,10],[13,23],[24,25]] 
B = [[1,5],[8,12],[15,24],[25,26]]
C = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
assert solution.get_intersections(A, B) == C





