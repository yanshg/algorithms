'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2

Explanation:
The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5

Explanation:
The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
'''

def get_lis_count(nums):
    # base cases
    if not nums:
        return 0
    
    n = len(nums)
    if n <= 1:
        return n
    
    # count[i]: the count of longest increasing sequence end with nums[i]
    # len[i]:   the length of longest increasing sequence end with nums[i]

    length = [ 1 ] * n
    count = [ 1 ] * n

    max_len = 1
    max_count = 1

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = 1
                elif length[j] + 1 == length[i]:
                    count[i] += 1
        
        if length[i] > max_len:
            max_len = length[i]
            max_count = count[i]
    
    # multiple sequences may have the max length
    print("legth: ", length)
    print("count: ", count)

    res = 0
    for i in range(n):
        if length[i] == max_len:
            res += count[i]

    return res

nums = [1,3,5,4,7]
assert get_lis_count(nums) == 2

nums = [2,2,2,2,2]
assert get_lis_count(nums) == 5
