'''

339. Nested List Weight Sum
1. Question
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list[[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list[1,[4,[6]]], return27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

'''

# [1, [4, [6]]]




def nested_list_sum(arr):
    if not arr:
        return 0
    
    def dfs(arr, depth=0):
        sum = 0
        if isinstance(arr, list):
            for num in arr:
                sum += dfs(num, depth + 1)
        else:
            sum += arr * depth
        return sum
    
    return dfs(arr)

arr = [1, [4, [6]]]
print(nested_list_sum(arr))

arr = [[1,1],2,[1,1]]
print(nested_list_sum(arr))