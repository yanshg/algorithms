'''
436. Find Right Interval
1. Question
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.

You may assume none of these intervals have the same start point.

Example 1:

Input: [ [1,2] ]
Output: [-1]


Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

Input: [ [3,4], [2,3], [1,2] ]
Output: [-1, 0, 1]


Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:

Input: [ [1,4], [2,3], [3,4] ]
Output: [-1, 2, -1]


Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

'''

def find_right_interval(intervals):
    starts = sorted([ (interval[0], i) for i, interval in enumerate(intervals) ])
    return [ get_left_most_insert_position(starts, interval[1]) for interval in intervals ]

def get_left_most_insert_position(starts, end):
    n = len(starts)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if starts[mid][0] == end:
            right = mid - 1
        elif starts[mid][0] < end:
            left = mid + 1
        elif starts[mid][0] > end:
            right = mid - 1
    
    if left >= n:
        return -1
    
    return starts[left][1]

intervals = [ [1,4], [2,3], [3,4] ]
assert find_right_interval(intervals) == [-1, 2, -1]

intervals = [ [3,4], [2,3], [1,2] ]
#print(find_right_interval(intervals))
assert find_right_interval(intervals) == [-1, 0, 1]

