'''
Given an integer N, construct all possible binary search trees with N nodes.
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: {self.left}, {self.right})"

def build_binary_search_tree(n):

    def build_tree(low, high, memo={}):
        if low > high:
            return [ None ]
        elif low == high:
            return [ Node(low) ]

        key = (low, high)
        if key in memo:
            return memo[key]
            
        res = []
        for i in range(low, high + 1):
            for left_tree in build_tree(low, i - 1, memo):
                for right_tree in build_tree(i+1, high, memo):
                    res += [ Node(i, left_tree, right_tree) ]

        memo[key] = res
        return res
    
    return build_tree(1, n, {})

print(build_binary_search_tree(0))
print(build_binary_search_tree(10))