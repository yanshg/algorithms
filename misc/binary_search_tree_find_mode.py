'''
 identify the value(s) that occur most frequently. Since a BST's in-order traversal gives a sorted sequence, this property can be used to count frequencies efficiently.
 '''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def find_modes(root):
    modes = []
    current_val = None
    current_count = 0
    max_count = 0

    def inorder(root):
        nonlocal modes, current_val, current_count, max_count
        if not root:
            return
        
        inorder(root.left)

        # count and compare to get modes
        if root.val == current_val:
            current_count += 1
        else:
            current_val = root.val
            current_count = 1

        if current_count > max_count:
            modes = [ current_val ]
            max_count = current_count
        elif current_count == max_count:
            modes.append(current_val)

        inorder(root.right)

    inorder(root)
    return modes


def find_modes_iterative(root):
    if not root:
        return []

    stack = []
    modes = []
    current_value = None
    current_count = 0
    max_count = 0

    # Iterative in-order traversal
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()

        # Process the current node
        if node.val == current_value:
            current_count += 1
        else:
            current_value = node.val
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            modes = [current_value]
        elif current_count == max_count:
            modes.append(current_value)

        node = node.right

    return modes

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

# Find mode
result = find_modes(root)
print("Modes in BST:", result)

result = find_modes_iterative(root)
print("Modes in BST:", result)