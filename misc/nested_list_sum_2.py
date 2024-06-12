'''
364. Nested List Weight Sum II
1. Question
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list[[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list[1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

'''

# [1, [4, [6]]]

def get_max_depth(arr):
    res = 0
    if isinstance(arr, list):
        for item in arr:
            res = max(res, 1 + get_max_depth(item))
    return res

from collections import defaultdict

def nested_list_sum(arr):
    if not arr:
        return 0
    
    max_depth = 0
    sum_of_depth_level = defaultdict(int)

    def dfs(arr, depth=0):
        nonlocal max_depth, sum_of_depth_level

        max_depth = max(max_depth, depth)

        if isinstance(arr, list):
            for item in arr:
                dfs(item, depth + 1)
        else:
            sum_of_depth_level[depth] += arr
    
    res = 0
    dfs(arr, 0)

    for i in range(1, max_depth + 1):
        res += ( sum_of_depth_level[i] * (max_depth - i + 1) )

    return res
    

arr = [1, [4, [6]]]
print(nested_list_sum(arr))

arr = [1, [4, [6]], [5, [6, [7]]]]
print(nested_list_sum(arr))

arr = [[1,1],2,[1,1]]
print(nested_list_sum(arr))