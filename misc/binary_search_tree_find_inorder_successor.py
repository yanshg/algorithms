'''
finding the inorder successor of a given node in a Binary Search Tree (BST). The challenge is to determine this using only the tree structure, without parent pointers.
'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: {self.left}, {self.right})"

def get_successor(root, p):
    if not root:
        return None
    
    successor = None
    while root:
        if p.val < root.val:
            # get potential successor
            successor = root
            root = root.left
        else:
            root = root.right

    return successor

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
print(root.val)

successor = get_successor(root, root.left)
if root.left and successor:
    print(root.left.val, successor.val)

successor = get_successor(root, root.right)
if root.right and successor:
    print(root.right.val, successor.val)