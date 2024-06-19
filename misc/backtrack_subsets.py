'''
Given a set of distinct integers,nums, return all possible subsets (the power set).

Note:The solution set must not contain duplicate subsets.

For example,
If nums=[1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

def get_subsets(nums):
    n = len(nums)
    res = []

    def backtrack(nums, start, subset, res):
        res += [ subset[:] ]
        
        for i in range(start, n):
            subset.append(nums[i])
            backtrack(nums, i+1, subset, res)
            subset.pop()

    backtrack(nums, 0, [], res)
    return res

nums = [ 1, 2, 3 ]
print(get_subsets(nums))