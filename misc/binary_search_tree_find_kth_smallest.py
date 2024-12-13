'''
finding the k-th smallest element in a Binary Search Tree (BST). The 

k-th smallest element corresponds to the k-th element in the in-order traversal of the BST, as it gives elements in sorted order.
'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find_kth_smallest(root, k):

    index = 0
    result = None
    def inorder(root):
        nonlocal index, result
        if not root:
            return None
        
        inorder(root.left)

        # compare index
        index += 1
        if index == k:
            result = root.val
            return

        inorder(root.right)

    inorder(root)
    return result

'''
       5
      / \
     3   6
    / \
   2   4
  /
 1
'''

# Construct the tree
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
root.right = TreeNode(6)

# Find the kth smallest element
k = 8
result = find_kth_smallest(root, k)
print(f"The {k}rd smallest element is:", result)
