"""

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"

def count_unival_trees(root):
    
    count = 0

    def is_unival_tree(root):
        nonlocal count
        # base case
        if not root:
            return True
    
        is_unival_tree_left = is_unival_tree(root.left)
        is_unival_tree_right = is_unival_tree(root.right)

        if is_unival_tree_left and is_unival_tree_right:
            if (root.left and root.left.val != root.val) or \
               (root.right and root.right.val != root.val):
                return False
            
            count += 1
            return True
        
        return False
    
    is_unival_tree(root)
    return count

root = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0)))
print(count_unival_trees(root))