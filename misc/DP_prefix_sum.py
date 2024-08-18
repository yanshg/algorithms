'''
Given an integer array nums, find the sum of the elements between indices i and j (i≤j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

You may assume that the array does not change.

There are many calls to sumRange function.

'''

# prefix_sum[0] = 0
# prefix_sum[1] = A[0]
# prefix_sum[2] = A[0] + A[1]
# prefix_sum[i] = A[0] + A[1] + ... + A[i-1]

# sum_range(i, j) = prefix_sum[j+1] - prefix_sum[i]

class PrefixSum:
    def __init__(self, nums):
        n = len(nums)
        self.prefix_sum = [ 0 ] * (n + 1)
        for i in range(1, n+1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]

    def sum_range(self, i, j):
        return self.prefix_sum[j+1] - self.prefix_sum[i]

nums = [-2, 0, 3, -5, 2, -1]
prefixsum = PrefixSum(nums)

print(prefixsum.sum_range(0, 2))

