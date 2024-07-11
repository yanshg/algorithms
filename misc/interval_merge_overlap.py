'''
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

'''

def remove_overlap_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))

    res = []
    for interval in intervals:
        last = res[-1] if res else None
        if not last or interval[0] > last[1]:
            # need convert tuple to list
            res += [ list(interval) ]
        else:
            last[1] = max(interval[1], last[1])

    print(res)
    return res

intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
assert remove_overlap_intervals(intervals) == [[1, 3], [4, 10], [20, 25]]