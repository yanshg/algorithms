'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''

def sum3_uniq(nums: list[int]) -> list[list[int]]:
    nums.sort()
    l = len(nums)

    res = []
    for i in range(l-2):
        # if value(nums[i]) was already processed
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, l - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res += [ [ nums[i], nums[left], nums[right] ] ]
                while left < right and nums[left+1] == nums[left]: left += 1
                while left < right and nums[right-1] == nums[right]: right -= 1
                left += 1
                right -= 1

    return res

nums = [-1, 0, 1, 1, 2, -1, -1, -4]
print(sum3_uniq(nums))