'''
Given an array of n positive integers and a positive integers, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

'''

def get_min_size_subarray_sum(nums, s):
    if not nums:
        return 0

    min_len = float('inf')

    sum = 0
    left = 0
    for right, n in enumerate(nums):
        sum += n

        while left <= right and sum >= s:
            min_len = min(min_len, right - left + 1)

            sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

nums = [2,3,1,2,4,3]
s = 7
print(get_min_size_subarray_sum(nums, s))