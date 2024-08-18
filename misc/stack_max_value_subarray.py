'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''

from collections import deque

def get_max_in_subarray_window(nums, k):
    res = []

    # use monotone stack/deque
    dq = deque([])
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        
        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

nums = [10, 5, 2, 7, 8, 7]
k = 3
print(get_max_in_subarray_window(nums, k))
