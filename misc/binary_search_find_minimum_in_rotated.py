'''
Problem Statement
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

Example
Input: nums = [2,2,2,0,1]
Output: 0
'''

def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

        #elif nums[mid] < nums[right]:
        #    right = mid
        #else:
        #    right -= 1
    
    return nums[left]

nums = [2,2,2,0,1]
assert findMin(nums) == 0
