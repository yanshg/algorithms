'''
1373. Maximum Sum BST in Binary Tree

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"
    
def get_maximum_sum_bst_in_binary_tree(root):
    max_sum = 0

    def get_bst(root):
        nonlocal max_sum

        if not root:
            return True, float('inf'), float('-inf'), 0
        
        #if not root.left and not root.right:
        #    max_sum = max(max_sum, root.val)
        #    return True, root.val, root.val, root.val
    
        is_bst_left, min_left, max_left, sum_left = get_bst(root.left)
        is_bst_right, min_right, max_right, sum_right = get_bst(root.right)

        if is_bst_left and is_bst_right and max_left <= root.val <= min_right:
            # tree with root is a BST
            sum1 = root.val + sum_left + sum_right
            max_sum = max(max_sum, sum1)

            # min(min_left, root.val)  <->  max(max_right, root.val)
            return True, min(min_left, root.val), max(max_right, root.val), sum1
    
        return False, 0, 0, 0
    
    get_bst(root)
    return max_sum

root = TreeNode(1, TreeNode(4, TreeNode(2), TreeNode(4)), TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6))))
print(get_maximum_sum_bst_in_binary_tree(root))

root = TreeNode(4, TreeNode(3, TreeNode(1), TreeNode(2)))
print(get_maximum_sum_bst_in_binary_tree(root))

root = TreeNode(-2, TreeNode(-4), TreeNode(-5))
print(get_maximum_sum_bst_in_binary_tree(root))
    

    
