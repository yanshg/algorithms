'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n

-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''

# O(n ^ 2), O(n)
def triplet_lis(nums):
    n = len(nums)

    # DP[i]: longest increasing sequence length of nums[:i+1]
    DP = [ 1 ] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                DP[i] = max(DP[i], DP[j] + 1)
                if DP[i] >= 3:
                    return True
    return False


def triplet_sequence(nums):
    if not nums or len(nums) < 3:
        return False
    
    min1, min2 = float('inf'), float('inf')
    for num in nums:
        if num < min1:
            min1 = num
        elif num < min2:
            min2 = num
        else:
            return True
    return False


nums = [1, 2, 3, 4, 5]
assert triplet_lis(nums)

nums = [5, 4, 3, 2, 1]
assert not triplet_lis(nums)

nums = [5, 4, 3, 2, 1]
assert not triplet_sequence(nums)

nums = [5, 4, 3, 2, 1, 2, 3]
assert not triplet_sequence(nums)
    