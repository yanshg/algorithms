'''
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def get_min_diff(root):
    prev = None
    min_diff = float('inf')

    # inorder
    def inorder(node):
        nonlocal min_diff, prev
        if not node:
            return
        
        inorder(node.left)

        if prev:
            min_diff = min(min_diff, node.val - prev.val)

        prev = node

        inorder(node.right)

    inorder(root)

    return min_diff

# Example Usage
# Construct BST:       4
#                     / \
#                    2   6
#                   / \
#                  1   3
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6)

# Find minimum absolute difference
result = get_min_diff(root)
print("Minimum Absolute Difference:", result)