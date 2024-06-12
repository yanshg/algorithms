def sum2_to_k_with_hash(nums, k):
    hashset = set()
    for num in nums:
        if k-num in hashset:
            return True
        hashset.add(num)
    return False

def sum2_to_k(nums: list[int], k: int) -> list[list[int]]:
    combs = []
    left = 0
    right = len(nums) - 1
    while left<right:
        s = nums[left] + nums[right]
        if s == k:
            combs += [[ nums[left], nums[right] ]]
            left += 1
            right -= 1
        elif s < k:
            left += 1
        elif s > k:
            right -= 1
        
    return combs


def sum3_to_k(nums, k):
    nums = sorted(nums)
    all_combs = []
    for n in nums:
        combs = sum2_to_k(nums, k)
        all_combs += [ [n, comb[0], comb[1]] for comb in combs ]
    return all_combs   

