'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
'''

'''
Solution:

To implement the next permutation, which rearranges numbers into the lexicographically next greater permutation, you can follow these steps:

Find the first decreasing element: Traverse the array from right to left and find the first element that is smaller than the element next to it.

Find the element to swap with: Traverse the array from right to left again and find the first element that is greater than the previously found element.

Swap the elements: Swap these two elements.

Reverse the remaining elements: Reverse the elements to the right of the initially found element to get the next permutation.

'''

def nextPermutation(nums):
    # Step 1: Find the first decreasing element
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find the element to swap with
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap the elements
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the remaining elements
    nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
