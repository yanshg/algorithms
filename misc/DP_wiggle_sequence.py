'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example,[1,7,4,9,2,5]is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast,[1,4,7,2,5]and[1,7,4,5,5]are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:

Input:
 [1,7,4,9,2,5]

Output:
 6
The entire sequence is a wiggle sequence.


Input:
 [1,17,5,10,13,15,10,5,16,8]

Output:
 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].


Input:
 [1,2,3,4,5,6,7,8,9]

Output:
 2
'''

# 2 dimensions of LIS

def wiggle_sequence(nums):
    if not nums:
        return 0
    
    n = len(nums)
    if n == 1:
        return 1

    res = 1

    # DP[i][0]: Longest wiggle sequence end with i-th element with decrease mode
    # DP[i][1]: Longest wiggle sequence end with i-th element with increase mode
    DP = [ [1, 1] for i in range(n) ]
    print(DP)
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and DP[j][0] + 1 > DP[i][1]:
                DP[i][1] = 1 + DP[j][0]
            elif nums[j] > nums[i] and DP[j][1] + 1 > DP[i][0]:
                DP[i][0] = 1 + DP[j][1]
    
        res = max(res, DP[i][0], DP[i][1])

    print(DP)
    return res

nums = [1,17,10,13,10,16,8]
assert wiggle_sequence(nums) == 7