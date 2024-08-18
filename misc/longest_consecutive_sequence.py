'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],

The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

# for each num, if num-1 not in the nums, which means num is the head of a new sequence

# O(n)
def get_longest_consecutive_sequence(nums):
    vset = set(nums)
    max_len = 1

    for i in nums:
        if i-1 not in vset:
            len = 1
            j = i
            while j+1 in vset:
                len += 1
                j += 1
            max_len = max(max_len, len)

    return max_len

nums = [100, 4, 200, 1, 3, 2]
assert get_longest_consecutive_sequence(nums) == 4
