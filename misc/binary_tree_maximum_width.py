'''
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where thenullnodes between the end-nodes are also counted into the length calculation.

Example 1:

Input:


           1
         /   \
        3     2
       / \\     \
      5   3     9 


Output:
 4

Explanation:
 The maximum width existing in the third level with the length 4 (5,3,null,9).

 Example 2:

Input:

          1
         /  
        3    
       / \
      5   3     

Output:
 2

Explanation:
 The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input:

          1
         / \
        3   2 
       /        
      5      

Output:
 2

Explanation:
 The maximum width existing in the second level with the length 2 (3,2).

 Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9 
     /         \
    6           7

Output:
 8

Explanation:
The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
Note:Answer will in the range of 32-bit signed integer.
'''

# BFS

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

from collections import deque

def get_maximum_width(root):
    # base case
    if not root:
        return 0
    
    max_width = 0

    # (node, pos)
    dq = deque([(root, 0)])

    while dq:
        start = dq[0][1]
        for _ in range(len(dq)):
            node, end = dq.popleft()
            max_width = max(max_width, end - start + 1)

            if node.left:
                dq.append((node.left, 2 * end + 1))
            if node.right:
                dq.append((node.right, 2 * end + 2))
    
    return max_width

'''
           1
         /   \
        3     2
       / \\     \
      5   3     9 
      
'''
root = Node(1, Node(3, Node(5), Node(3)), Node(2, None, Node(9)))
print(get_maximum_width(root))

'''
          1
         / \
        3   2 
       /        
      5      
'''
root = Node(1, Node(3, Node(5)), Node(2))
print(get_maximum_width(root))


'''
          1
         / \
        3   2
       /     \
      5       9 
     /         \
    6           7
'''
root = Node(1, Node(3, Node(5, Node(6))), Node(2, None, Node(9, None, Node(7))))
print(get_maximum_width(root))

