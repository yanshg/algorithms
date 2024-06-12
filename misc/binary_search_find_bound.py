
def find_left_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            right = mid - 1

    if left >= len(nums) or nums[left] != target:
        return -1

    return left

def find_right_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left = mid + 1

    if right < 0 or nums[right] != target:
        return -1

    return right


def find_left_bound1(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] >= target:
            right = mid

    if left >= len(nums) or nums[left] != target:
        return -1

    return left

nums = [ 1, 2, 2, 2, 2, 3, 3, 3, 4 ]

assert find_left_bound(nums, 2) == 1
assert find_right_bound(nums, 2) == 4

assert find_left_bound1(nums, 2) == 1
