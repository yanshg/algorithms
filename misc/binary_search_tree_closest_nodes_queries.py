'''
2476. Closest Nodes Queries in a Binary Search Tree

You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.


Bisect.bisect_right(a, x).  Return 0 if x < min(a), return len(a) if x > max(a).    所在 index -1 的 值 <= x
Bisect.bisect_left(a, x).   Return 0 if x < min(a), return len(a) if x > max(a).    所在 index 的 值 >= x

利用此性质可以求 array 中该值的上下区间。

'''

from bisect import bisect_left, bisect_right

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"

def get_closest_queries(root: TreeNode, queries: list[int]) -> list[list[int]]:
    if not root or not queries:
        return []
    
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [ node.val ] + inorder(node.right)

    sorted_values = inorder(root)

    res = []
    for query in queries:
        idx1 = bisect_right(sorted_values, query) - 1
        idx2 = bisect_left(sorted_values, query)

        # Determine floor and ceil values
        floor = sorted_values[idx1] if idx1 >= 0 else -1
        ceil = sorted_values[idx2] if idx2 < len(sorted_values) else -1

        res += [ [floor, ceil] ]

    return res

root = TreeNode(6, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(13, TreeNode(9), TreeNode(15, TreeNode(14))))
print(root)

queries = [ 2, 5, 16]
print(get_closest_queries(root, queries))