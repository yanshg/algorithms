'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def get_bst_sum(root, L, R):
    if not root:
        return 0
    
    if root.val < L:
        return get_bst_sum(root.right, L, R)
    
    if root.val > R:
        return get_bst_sum(root.left, L, R)
    
    return root.val + get_bst_sum(root.left, L, R) + get_bst_sum(root.right, L, R)

root = Node(5, Node(3), Node(6))
print(get_bst_sum(root, 4, 5))