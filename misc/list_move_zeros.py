def move_zeros(nums: list[int]) -> list[int]:
    last_zero_index = 0
    for num in nums:
        if num != 0:
            nums[last_zero_index] = num
            last_zero_index += 1

    for i in range(last_zero_index, len(nums)):
        nums[i] = 0
    
    return nums

nums = [ 1, 0, 2, 0, 3 ]
print(move_zeros(nums))

    