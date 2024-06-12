'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums=[1,1,1,2,2,3],

Your function should return length =5, with the first five elements of nums being 1,1,2,2 and 3. It doesn't matter what you leave beyond the new length.

'''

def remove_duplicated_nums(nums, most_count):
    slow = 0
    count = 0
    for fast,num in enumerate(nums):
        if num != nums[slow]:
            nums[slow] = num
            slow += 1
            count = 1
        elif count < most_count:
            nums[slow] = num
            slow += 1
            count += 1

    print(nums)
    return slow

nums = [ 1, 1, 1, 2, 2, 3, 3, 3, 3, 4 ]
print(remove_duplicated_nums(nums, 2))