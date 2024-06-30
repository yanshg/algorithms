'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols+and-. For each integer, you should choose one from+and-as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Copy
Input: nums is [1, 1, 1, 1, 1], S is 3. 

Output: 5

Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

'''

# 0-1 Knapsack issue

def sum_target_ways(nums, k):
    if not nums:
        return 0
    
    total = sum(nums)
    if k > total or k < -total or (total + k) % 2 != 0:
        return 0
    
    target = (total + k) // 2

    def knapsack01(nums, target):
        n = len(nums)

        DP = [0] * (target + 1)
        DP[0] = 1
        print(DP)
        for i in range(n):
            for j in reversed(range(target+1)):
                if j >= nums[i]:
                    DP[j] += DP[j-nums[i]]
            print(DP)
        return DP[target]

    return knapsack01(nums, target)

nums = [1,1,1,1,1]
k = 3
print(sum_target_ways(nums, k))
