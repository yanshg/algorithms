'''
'''
class Solution:
    def minMeetingRooms(self, intervals):
        starts = [ (t[0], 1) for t in intervals ]
        ends = [ (t[1], -1) for t in intervals]

        all = starts + ends
        all.sort(key = lambda x: (x[0], x[1]))

        res = 0
        rooms = 0
        for t in all:
            rooms = rooms + t[1]
            res = max(res, rooms)

        return res

solution=Solution()
intervals = [[0,30], [5,10], [15,20]]
print(solution.minMeetingRooms(intervals))

intervals = [[0,30], [5,50], [15,34], [35,55], [36,39], [41,60]]
print(solution.minMeetingRooms(intervals))
