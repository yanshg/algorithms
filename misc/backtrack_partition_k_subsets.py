
'''

698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.


Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true

Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

'''

from collections import defaultdict

class Solution1:

    # O(K^N)
    def canPartitionKSubsets(self, nums, k):
        
        def is_valid(buckets, target):
            for bucket in buckets:
                if len(bucket) == 0 or sum(bucket) != target:
                    return False
            return True
        
        def backtrack(nums, i, buckets, target):
            if i==len(nums) and is_valid(buckets, target):
                print(buckets)
                return True

            num = nums[i]
            
            for bucket in buckets:
                sum1 = sum(bucket)
                if sum1 + num > target:
                    continue
                
                bucket.append(num)
                if backtrack(nums, i+1, buckets, target):
                    return True
                bucket.pop()

            return False
        
        if len(nums) < k: return False
        
        sum1 = sum(nums)
        if sum1%k > 0: return False
        
        target = sum1 // k
        
        nums.sort(reverse=True)
        buckets = [ [] for i in range(k) ]
        return backtrack(nums, 0, buckets, target)


class Solution2:
    def canPartitionKSubsets(self, nums, k):
        def backtrack(i, curr_sum, k, nums, taken, target):
            if i == k-1: 
                print(taken)
                return True
            
            if curr_sum > target:
                return False

            if curr_sum == target:
                return backtrack(i+1, 0, k, nums, taken, target)

            for j, num in enumerate(nums):
                if taken[j] == 1:
                    continue
                                    
                taken[j] = 1
                
                if backtrack(i, curr_sum+num, k, nums, taken, target):
                    return True

                taken[j] = 0
            
            return False
        
        if len(nums)<k: return False
        
        sum1 = sum(nums)
        if sum1 % k > 0: return False
        
        target = sum1 // k
        
        taken = [0] * len(nums)
        nums.sort(reverse=True)
        
        return backtrack(0, 0, k, nums, taken, target)
        

class Solution3:
    def canPartitionKSubsets(self, nums, k):
        def backtrack(i, curr_sum, k, nums, taken, target, memo):
            if i == k-1: 
                print(memo)
                memo[taken] = True
                return True
            
            if taken in memo:
                return memo[taken]

            if curr_sum > target:
                memo[taken] = False
                return False

            if curr_sum == target:
                return backtrack(i+1, 0, k, nums, taken, target, memo)

            for j, num in enumerate(nums):
                if (taken>>j & 1) == 1:
                    continue
                                    
                taken |= 1<<j
                
                if backtrack(i, curr_sum+num, k, nums, taken, target, memo):
                    memo[taken] = True
                    return True

                taken &= ~(1<<j)
            
            memo[taken] = False
            return False
        
        if len(nums)<k: return False
        
        sum1 = sum(nums)
        if sum1 % k > 0: return False
        
        target = sum1 // k
        
        nums.sort(reverse=True)
        taken = 0
        memo = dict()
        
        return backtrack(0, 0, k, nums, taken, target, memo)
        

class Solution4:
    def canPartitionKSubsets(self, nums, k):
        n, s = len(nums), sum(nums)
        if n < k or s % k > 0: 
            return False

        target = s // k
        used = [0] * n
        memo = defaultdict(bool)

        # make the subset_sum quickly larger than target, and fail earlier.
        nums.sort(reverse=True)

        # k:  kth bucket
        # i:  i-th - last items for kth bucket
        # used:  0 - un-used,  1 - used
        def backtrack(k, i, subset_sum, used, memo):
            # need convert used array to tuple so that it could be used as a key.
            key = tuple(used)

            # Need not check if k == 0
            # Check k == 1 means the remaining nums in first bucket should be also sum to k.
            if k == 1:
                memo[key] = True
                return True

            if subset_sum == target:
                return backtrack(k-1, 0, 0, used, memo)

            if key in memo:
                return memo[key]
            
            for j in range(i, n):
                if used[j] or subset_sum + nums[j] > target:
                    continue
                
                used[j] = 1
                if backtrack(k, i+1, subset_sum + nums[j], used, memo):
                    return True
                used[j] = 0

            memo[key] = False
            return False

        return backtrack(k, 0, 0, used, memo)

solution = Solution4()

nums = [4,3,2,3,5,2,1]
k = 4
assert solution.canPartitionKSubsets(nums, k)

nums = [1,1,1,1,2,2,2,2]
k = 4
assert solution.canPartitionKSubsets(nums, k)

nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
k = 5
assert solution.canPartitionKSubsets(nums, k)



