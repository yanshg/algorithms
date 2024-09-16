class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def get_right_view(root):
    res = []
    dq = deque([root])
    while dq:
        res += [ dq[-1].val ]
        for _ in range(len(dq)):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return res

root = Node(12, Node(6, Node(5), Node(9)), Node(14, Node(10)))
print(get_right_view(root))