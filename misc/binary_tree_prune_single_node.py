"""
This problem was asked by Yahoo.

Recall that a full binary tree is one in which each node is either a leaf node, or has two children. Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

         0
      /     \
    1         2
  /            \
3                 4
  \\             /   \
    5          6     7
You should convert it to:

     0
  /     \
5         4
        /   \
       6     7

"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}: ({self.left}), ({self.right})"

def prune_single_node_tree(root):
    # base cases:  None, or leaf node
    if not root:
        return root
    
    root.left = prune_single_node_tree(root.left)
    root.right = prune_single_node_tree(root.right)

    # if leaf node or have both left and right child.
    if (not root.left and not root.right) or \
        (root.left and root.right):
        return root
    
    return root.left if root.left else root.right

root = Node(0, Node(1, Node(3, None, Node(5))), Node(2, None, Node(4, Node(6), Node(7))))
print(root)


print(prune_single_node_tree(root))