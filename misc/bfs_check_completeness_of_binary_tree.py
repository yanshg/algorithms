'''
To check if a binary tree is complete, you can use a level-order traversal (BFS). A binary tree is complete if every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.


'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_complete_binary_tree(root):
    if not root:
        return True

    queue = deque([root])
    end = False  # flag to mark the encounter of the first incomplete node

    while queue:
        node = queue.popleft()
        if not node:
            end = True
        else:
            if end:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(is_complete_binary_tree(root))  # Output: True
