'''
Given an integer array nums and an integer k, return the (k)th largest element in the array. Note that it is the (k)th largest element in the sorted order, not the (k)th distinct element.

Example

Input:
nums = [3,2,1,5,6,4]
k = 2
'''

import heapq

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
