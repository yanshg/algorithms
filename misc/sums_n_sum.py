'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:

    Input: nums = []
    Output: []

Example 3:

    Input: nums = [0]
    Output: []

'''

def sum_target(nums, n, target):

    def two_sum(nums, left, right, target):
        res = []
        while left < right:
            nl, nr = nums[left], nums[right]
            sum = nl + nr
            if sum == target:
                res += [ [nl, nr ] ]
                while left<right and nums[left]==nl: left += 1
                while left<right and nums[right]==nr: right -= 1
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return res

    def n_sum(nums, n, left, right, target):
        res = []

        if n > 2:
            i = left
            while i<=right-n+1:
                #res += [ [ nums[i] ] + result for result in n_sum(nums, n-1, i+1, right, target-nums[i]) if result ]
                for result in n_sum(nums, n-1, i+1, right, target-nums[i]):
                    if result:
                        res += [ [ nums[i] ] + result ]
                while i<=right-n+1 and nums[i+1]==nums[i]: i+=1
                i += 1
        elif n == 2:
            res += two_sum(nums, left, right, target)

        return res

    if not nums or n<2 or len(nums)<n:
        return []

    nums.sort()
    return n_sum(nums, n, 0, len(nums)-1, target)

# For two_sum():   O(NlogN) + O(N)
# For 3_sum():     O(NlogN) + O(N^2)

nums = [0,0,0]
result = sum_target(nums, 3, 0)
print(result)

nums = [-1,0,1,2,-1,-4]
assert sum_target(nums, 3, 0) == [[-1,-1,2],[-1,0,1]]
