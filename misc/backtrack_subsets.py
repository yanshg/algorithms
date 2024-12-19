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

def get_subsets_iteration(nums):
    result = [ [] ]
    for num in nums:
        result += [ subset + [num] for subset in result ]
    return result

def get_subsets_backtrack(nums):
    result = []

    def backtrack(start, subset, result):
        result += [ subset[:] ]

        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset, result)
            subset.pop()
    
    backtrack(0, [], result)
    return result

nums = [ 1, 2, 3 ]
print(get_subsets_iteration(nums))
print(get_subsets_backtrack(nums))