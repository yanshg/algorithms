'''
Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def count_complete_tree(root):
    # base case
    if not root:
        return 0
    
    left_depth = 0
    p = root
    while p:
        p = p.left
        left_depth += 1

    right_depth = 0
    p = root
    while p:
        p = p.right
        right_depth += 1

    print(left_depth, right_depth)
    print(1<<left_depth)
    if left_depth == right_depth:
        return (1<<left_depth) - 1
    
    return 1 + count_complete_tree(root.left) + count_complete_tree(root.right)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node3
print(count_complete_tree(node1))
    