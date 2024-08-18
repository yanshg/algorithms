'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

def get_permutation(nums):
    res = []
    used = set()

    def backtrack(nums, bucket, used, res):
        if len(bucket) == len(nums):
            res += [ bucket[:] ]
            return
        
        for i, num in enumerate(nums):
            # after previous num and come back,  used[i-1] will be cleaned.
            if i > 0 and nums[i-1] == nums[i] and i-1 not in used:
                continue
            
            if i not in used:            
                used.add(i)
                bucket.append(num)
                backtrack(nums, bucket, used, res)
                bucket.pop()
                used.discard(i)
    
    nums.sort()
    backtrack(nums, [], used, res)
    return res

nums = [ 1, 1, 2 ]
print(get_permutation(nums))