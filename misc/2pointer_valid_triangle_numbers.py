'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: [2,2,3,4]
Output: 3

Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

'''

def get_count_of_triangle_numbers(nums):
    nums.sort()
    l = len(nums)
    
    count = 0
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if nums[i] + nums[j] > nums[k]:
                    count += 1

    return count

nums = [2,2,3,4]
print(get_count_of_triangle_numbers(nums))