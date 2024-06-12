def sum_2(nums, left, right, target):

    while left < right:
        sum2 = nums[left] + nums[right]
        if sum2 < target:
            left += 1
        elif sum2 > target:
            right -= 1
        else:
            return [ nums[left], nums[right] ]
        
    return None
    
def sum_n(nums, n, left, right, target):
    if n == 2:
        return sum_2(nums, left, right, target)
    elif n > 2:
        for i in range(left, right + 1):
            num0 = nums[i]
            res = sum_n(nums, n - 1, i + 1, right, target - num0)
            if res:
                return [num0] + res       
    return None

def sum_n_main(nums, n, target):
    nums.sort()
    return sum_n(nums, n, 0, len(nums) - 1, target)

nums = [ 4, 3, 7, 2, 6, 3]
print(sum_n_main(nums, 3, 11))
print(sum_n_main(nums, 5, 18))


