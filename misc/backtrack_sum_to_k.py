'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k= 3,n= 7
Output:
[[1,2,4]]

Example 2:

Input: k= 3,n= 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]

'''

def get_combinations(k, target):
    
    def backtrack(start, k, target, bucket, res):
        sum1 = sum(bucket)
        if sum1 > target:
            return
        
        if k == 0 and sum1 == target:
            res += [ bucket[:] ]
            return
        
        if k <= 0:
            return
        
        for i in range(start, 10):
            bucket.append(i)
            backtrack(i+1, k-1, target, bucket, res)
            bucket.pop()

    res = []
    backtrack(1, k, target, [], res)
    return res

print(get_combinations(3, 7))
print(get_combinations(3, 9))