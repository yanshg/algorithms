"""

Given the root of a binary tree, you need to return a list of top-to-bottom orderings for each column index, starting from the leftmost column and ending on the rightmost column. If multiple nodes are in the same row and column, they should be sorted by their values.

"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> ({self.left}) ({self.right})"
    
from collections import defaultdict, deque

def get_vertical_view(root):
    columns = defaultdict(list)
    
    dq = deque([(root, 0)])
    while dq:
        print(dq)
        node, col = dq.popleft()
        columns[col].append(node.val)
        if node.left:
            dq.append((node.left, col - 1))
        if node.right:
            dq.append((node.right, col + 1))

    return [ columns[i] for i in sorted(columns.keys()) ]

root = Node(12, Node(6, Node(5), Node(9)), Node(14, Node(10)))
print(get_vertical_view(root))


        



