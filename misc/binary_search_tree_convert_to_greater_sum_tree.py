'''
To convert a Binary Search Tree (BST) into a Greater Sum Tree (GST), each node's value is replaced with the sum of all values in the original BST that are greater than or equal to the current node's value. 


This can be efficiently done using a reverse in-order traversal (right -> node -> left), since the traversal order processes nodes from the largest to the smallest value.


Algorithm:

Reverse In-Order Traversal:
Traverse the right subtree first, then the current node, and finally the left subtree.

This ensures nodes are processed in descending order of their values.

Maintain a Running Sum:

Keep a running_sum variable to accumulate the sum of all nodes processed so far.

Update each node's value by adding the running_sum to its original value and updating the running_sum.


'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"
    
def convert_bst_to_gst(root):

    running_sum = 0

    def reverse_inorder(node):
        nonlocal running_sum

        # base case
        if not node:
            return
        
        reverse_inorder(node.right)

        running_sum += node.val
        node.val = running_sum

        reverse_inorder(node.left)
    
    reverse_inorder(root)
    return root
    

# Example Usage
# Construct a BST:       4
#                       / \
#                      1   6
#                     / \ / \
#                    0  2 5  7
#                       \     \
#                        3     8
root = TreeNode(4)
root.left = TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3)))
root.right = TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))
print(root)

gst_root = convert_bst_to_gst(root)
print(gst_root)