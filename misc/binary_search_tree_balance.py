'''
transform an unbalanced BST into a height-balanced BST. A height-balanced BST is a binary tree where the depth of the two subtrees of every node never differs by more than one.
'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"

def get_inorder_list(root):
    if not root:
        return []
    
    return get_inorder_list(root.left) + [ root.val ] + get_inorder_list(root.right)

def create_balanced_bst(arr):
    if not arr:
        return None
    
    l = len(arr)
    mid = l // 2

    root = TreeNode(arr[mid])
    root.left = create_balanced_bst(arr[:mid])
    root.right = create_balanced_bst(arr[mid+1:])
    return root

def transform_bst_to_balanced(root):

    items = get_inorder_list(root)
    return create_balanced_bst(items)

'''
       6
      / \
     2   8
    / \
   2   4
        \
         4
'''
# Construct the tree
root = TreeNode(6)
root.left = TreeNode(2, TreeNode(2), TreeNode(4, None, TreeNode(4)))
root.right = TreeNode(8)

print(root)

print(transform_bst_to_balanced(root))