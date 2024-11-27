'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}, {self.right})"

def recover_bst(root):

    prev = Node(float('-inf'))
    first, second = None, None

    def inorder(node):
        nonlocal prev, first, second

        # base case
        if not node:
            return
        
        inorder(node.left)

        if not first and prev.val >= node.val:
            first = prev
        if first and prev.val >= node.val:
            second = node

        prev = node

        inorder(node.right)

    inorder(root)

    if first and second:
        first.val, second.val = second.val, first.val

root = Node(1, Node(3, None, Node(2)))
print(root)
recover_bst(root)
print(root)