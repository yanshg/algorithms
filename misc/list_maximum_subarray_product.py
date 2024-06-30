'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

'''

def get_maximum_subarray_product(nums):
    # base cases
    if not nums:
        return 0
    
    max_ending_here = nums[0]
    min_ending_here = nums[0]
    max_so_far = max_ending_here

    for i in range(1, len(nums)):
        num = nums[i]
        print("num: ", num)
        print("before max_ending_here: ", max_ending_here)
        print("before min_ending_here: ", min_ending_here)

        if num > 0:
            max_ending_here = max(num, max_ending_here * num)
            min_ending_here = min(num, min_ending_here * num)
        else:
            temp = max_ending_here
            max_ending_here = max(num, min_ending_here * num)
            min_ending_here = min(num, temp * num)
        print("after max_ending_here: ", max_ending_here)
        print("after min_ending_here: ", min_ending_here)
        print("\n")
        
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

nums = [-2,3,-3,4]
print(get_maximum_subarray_product(nums))
