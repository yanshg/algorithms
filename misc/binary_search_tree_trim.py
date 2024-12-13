'''
669. Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"


# inorder
def trim_bst(root, low, high):
    # base case
    if not root:
        return None

    if root.val < low:
        # remove root and root.left
        # return trim result of right subtree
        return trim_bst(root.right, low, high)
    
    if root.val > high:
        # remove root and root.right
        # return trim result of left subtree
        return trim_bst(root.left, low, high)
    
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    
    return root

root = TreeNode(1, TreeNode(0), TreeNode(2))
print(root)

low, high = 1, 2
new_root = trim_bst(root, low, high)
print(new_root)

root = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
print(root)

low, high = 1, 3
new_root = trim_bst(root, low, high)
print(new_root)