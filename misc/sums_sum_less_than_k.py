'''

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

 Example 1:

 Input: nums = [34,23,1,24,75,33,54,8], k = 60
 Output: 58
 Explanation: We can use 34 and 24 to sum 58 which is less than 60.
 Example 2:

 Input: nums = [10,20,30], k = 15
 Output: -1
 Explanation: In this case it is not possible to get a pair sum less that 15.

'''

class Solution:

    def two_sum_less_than_k(self, nums, k):
        nums.sort()
        left, right = 0, len(nums) - 1
        res = -1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                res = max(res, sum)
                left += 1
            else:
                right -= 1
        return res

solution = Solution()
assert solution.two_sum_less_than_k([34,23,1,24,75,33,54,8], 60) == 58
