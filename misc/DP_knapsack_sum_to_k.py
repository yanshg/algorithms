'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

Copy
nums = [1, 2, 3]

target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

'''

def sum_to_target_ways(nums, target):
    # DP[i][j]:  means combinations for nums[:i+1] sum to j
    #
    # DP[i][j] = DP[i-1][j]         +     DP[i-1][j - num[i]]
    #            exclude nums[i],         include nums[i]

    # DP[0][j] = 0 for j > 0
    # DP[i][0] = 0 for i > 0
    # DP[0][0] = 1

    # Unbounded Knapsack issue

    # We can use Knapsack template which use 1-dimension DP

    DP = [ 0 ] * (target + 1)
    DP[0] = 1

    for j in range(1, target + 1):
        for num in nums:
            if j >= num:
                DP[j] += DP[j - num]
        print(DP)
    
    return DP[-1]


nums = [1, 2, 3]
target = 4
print(sum_to_target_ways(nums, target))