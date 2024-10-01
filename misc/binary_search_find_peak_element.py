
'''
finding a peak element in a given array. A peak element is defined as an element that is strictly greater than its neighbors. If the array contains multiple peaks, you can return the index of any of the peaks.
'''

def findPeakElement(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage
nums = [1, 2, 3, 1]
print(findPeakElement(nums))  # Output: 2

nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))  # Output: 5
