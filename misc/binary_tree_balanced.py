'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def check_if_height_balanced(root):
    is_balanced = True

    def get_depth(root):
        if not root:
            return 0
        
        nonlocal is_balanced

        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        if abs(left_depth - right_depth) > 1:
            is_balanced = False

        return 1 + max(left_depth, right_depth)
    
    get_depth(root)
    return is_balanced

root = Node(1, Node(2, Node(3)), Node(4))
print(check_if_height_balanced(root))