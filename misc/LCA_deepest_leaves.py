'''
finding the lowest common ancestor (LCA) of the deepest leaves in a binary tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcaDeepestLeaves(root: TreeNode) -> TreeNode:
    def dfs(node):
        if not node:
            return (0, None)
        
        left_depth, left_lca = dfs(node.left)
        right_depth, right_lca = dfs(node.right)
        
        if left_depth > right_depth:
            return (left_depth + 1, left_lca)
        elif right_depth > left_depth:
            return (right_depth + 1, right_lca)
        else:
            return (left_depth + 1, node)
    
    return dfs(root)[1]

# Example usage
# Constructing the binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(lcaDeepestLeaves(root).val)  # Output: 2
