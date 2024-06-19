# backtrack

def get_permutation_k(k):
    res = []
    nums = set(range(4))

    # bucket to hold the current permutation,

    def backtrack(k, nums, bucket = [], res = []):
        if len(bucket) > k:
            return
        
        if len(bucket) == k:
            res += [ bucket[:] ]
            return
        
        for num in nums:
            bucket.append(num)
            backtrack(k, nums - {num}, bucket, res)
            bucket.pop()

    backtrack(k, nums, [], res)
    return res

print(get_permutation_k(2))

    