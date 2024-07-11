'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

'''

def get_trapped_rain(heights):
    left, right = 0, len(heights) - 1
    max_height = 0
    res = 0

    while left <= right:
        if heights[left] < heights[right]:
            max_height = max(max_height, heights[left])
            res += max_height - heights[left]
            left += 1
        else:
            max_height = max(max_height, heights[right])
            res += max_height - heights[right]
            right -= 1
    return res


heights = [2, 1, 2]
assert get_trapped_rain(heights) == 1

heights = [3, 0, 1, 3, 0, 5]
assert get_trapped_rain(heights) == 8
