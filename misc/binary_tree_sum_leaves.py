"""
Meta:

A binary tree, which I need to return the sums of all paths up to the root. For example: 

      7 
    /   \
   3     2
  / \\   / \
 5   6 8   9 
 
 I need to return: 729+728+736+735= and make a sum.

"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}). ({self.right}))"
    
def sum_leaves(root):

    leaves = []

    def dfs(root, path, leaves):
        # base case
        if not root:
            return

        path = path * 10 + root.val

        # leaf node
        if not root.left and not root.right:
            leaves += [ path ]
            return

        dfs(root.left, path, leaves)
        dfs(root.right, path, leaves)

    dfs(root, 0, leaves)
    return sum(leaves)

root = Node(7, Node(3, Node(5), Node(6)), Node(2, Node(8), Node(9)))
print(root)
print(sum_leaves(root))
