"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]."
"""

def product_except_self(nums: list[int]) -> list[int]:
    l = len(nums)
    output = [ 1 ] * l

    left_product = 1
    for i in range(l):
        output[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in reversed(range(l)):
        output[i] *= right_product
        right_product *= nums[i]

    return output

nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]