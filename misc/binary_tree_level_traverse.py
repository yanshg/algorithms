'''
Given a binary tree, return thelevel ordertraversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''

class Node:
    def __init__(self, val , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
from collections import deque

def traverse_level_bfs(root):
    res = []
    dq = deque([root])
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            level.append(node.val)

            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        res.append(level)

    return res

def traverse_level_dfs(root):
    res = []
    def dfs(root, level = 0, res = []):
        if not root:
            return
        
        if len(res) == level:
            res.append([])

        res[level].append(root.val)

        dfs(root.left, level + 1, res)
        dfs(root.right, level + 1, res)

    dfs(root, 0, res)
    return res

root = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(root)
print(traverse_level_bfs(root))
print(traverse_level_dfs(root))