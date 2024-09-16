"""
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}: ({self.left}), ({self.right})"
    

def prune_all_zeros_subtree(root):
    # base cases:  None, or leaf node with 0
    if not root:
        return root
    
    root.left = prune_all_zeros_subtree(root.left)
    root.right = prune_all_zeros_subtree(root.right)

    if not root.left and not root.right and root.val == 0:
        return None

    return root 

root = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))
print(root)

print(prune_all_zeros_subtree(root))