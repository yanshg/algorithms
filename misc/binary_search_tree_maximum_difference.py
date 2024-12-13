'''
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def get_max_diff(root):

    def dfs(root, min_so_far, max_so_far):

        if not root:
            return max_so_far - min_so_far
        
        min_so_far = min(root.val, min_so_far)
        max_so_far = max(root.val, max_so_far)

        left_diff = dfs(root.left, min_so_far, max_so_far)
        right_diff = dfs(root.right, min_so_far, max_so_far)

        return max(left_diff, right_diff)

    return dfs(root, root.val, root.val)

# Example Usage
# Construct BST:       4
#                     / \
#                    2   6
#                   / \
#                  1   3
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6)

# Find maximum difference
result = get_max_diff(root)
print("Maximum Difference:", result)