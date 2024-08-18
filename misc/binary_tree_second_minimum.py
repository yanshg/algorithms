'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactlytwoorzerosub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:

    2
   / \
  2   5
     / \
    5   7


Output:
 5

Explanation:
The smallest value is 2, the second smallest value is 5.

Example 2:

Input:

    2
   / \
  2   2


Output:
 -1

Explanation:
The smallest value is 2, but there isn't any second smallest value.

'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def get_second_minimum(root):
    min1, min2 = float('inf'), float('inf')

    def dfs(root):
        if not root:
            return
        
        # adjust min1 and min2 according to current val.
        nonlocal min1, min2
        if root.val < min1:
            min2 = min1
            min1 = root.val            
        elif root.val < min2:
            min2 = root.val

        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return min2 if min2 != float('inf') else -1

root = Node(2, Node(2), Node(2))
print(get_second_minimum(root))

root = Node(2, Node(5, Node(5), Node(7)))
print(get_second_minimum(root))