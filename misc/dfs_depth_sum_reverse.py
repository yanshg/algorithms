'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

'''

from collections import defaultdict

def get_depth_sum_reverse(arr: list[int]) -> int:
    if not arr:
        return 0
    
    depth_map = defaultdict(list)

    def get_depth_map_dfs(arr, depth_map, depth=0):
        if not arr:
            return
        
        if isinstance(arr, list):
            for item in arr:
                get_depth_map_dfs(item, depth_map, depth+1)
        elif isinstance(arr, int):
            depth_map[depth].append(arr)

    get_depth_map_dfs(arr, depth_map, 0)
    #print(depth_map)
    depths = depth_map.keys()
    if not depths:
        return 0
    
    max_depth = max(depths)
    depth_sum = 0
    for depth in depths:
        for item in depth_map[depth]:
            depth_sum += (item * (max_depth - depth + 1))

    return depth_sum

assert get_depth_sum_reverse([[1,1],2,[1,1]]) == 8
assert get_depth_sum_reverse([1,[4,[6]]]) == 17