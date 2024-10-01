'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The subarrays [1,1] and [1,1] both sum to 2.

'''

def subarraySum(nums, k):
    count = 0
    sum = 0
    prefix_sums = {0: 1}
    
    for num in nums:
        sum += num
        if sum - k in prefix_sums:
            count += prefix_sums[sum - k]
        prefix_sums[sum] = prefix_sums.get(sum, 0) + 1
    
    return count

nums = [1,1,1,1,1]
k = 2
print(subarraySum(nums, k))