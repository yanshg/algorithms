'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si% Sj= 0 or Sj% Si= 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)

Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''

def get_longest_divisible_subset(nums):
    if not nums:
        return []
    
    n = len(nums)
    if n <= 1:
        return nums
    
    max_len = 0
    max_index = -1

    nums.sort()

    # [ length of longest divisible subset, index of previous item (-1 means None)]
    DP = [ [1, -1] for i in range(n) ]

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and DP[j][0] + 1 > DP[i][0]:
                DP[i][0] = DP[j][0] + 1
                DP[i][1] = j
        if DP[i][0] > max_len:
            max_len = DP[i][0]
            max_index = i

    print(DP)
    res = []
    index = max_index
    while index != -1:
        res.append(nums[index])
        index = DP[index][1]

    return list(reversed(res))

nums = [1, 2, 3, 4, 8]
#print(get_longest_divisible_subset(nums))
assert get_longest_divisible_subset(nums) == [1,2,4,8]