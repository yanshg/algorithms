'''

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:

Given binary tree

          1
         / \
        2   3
       / \
      4   5

Returns[4, 5, 3], [2], [1].

Explanation:

Removing the leaves [4, 5, 3] would result in this tree:
          1
         / 
        2

Now removing the leaf [2] would result in this tree:

          1
Now removing the leaf [1] would result in the empty tree:

          []

Returns [4, 5, 3], [2], [1].
'''
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

def get_leaves(root):
    res = []

    def dfs(root, res):
        if not root:
            return 0
        
        left_depth = dfs(root.left, res)
        right_depth = dfs(root.right, res)
        depth = 1 + max(left_depth, right_depth)

        # leaves' depth should be 1, and need add to res[0]
        if len(res) < depth:
            res.append([])
        res[depth-1].append(root.val)

        return depth
    
    dfs(root, res)
    return res

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print(root)
print(get_leaves(root))