'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundaryis defined as the path from root to the left-most node.Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Copy
Input:

  1
   \
    2
   / \
  3   4


Output:
[1, 3, 4, 2]

Explanation:

The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].

Example 2

Input:

    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  


Output:
[1,2,4,7,8,9,10,6,3]

Explanation:

The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    

def get_boundary(root):
    if not root:
        return None
    
    res = []
    res.append(root.val)
    get_side_boundary(root.left, res, isLeft = True)
    get_leafs(root, res)
    get_side_boundary(root.right, res, isLeft = False)

    return res

def get_side_boundary(root, res, isLeft = True):
    if not root or (not root.left and not root.right):
        return
    
    if isLeft:
        res.append(root.val)
        if root.left:
            get_side_boundary(root.left, res, isLeft)
        else:
            get_side_boundary(root.right, res, isLeft)
    else:
        if root.right:
            get_side_boundary(root.right, res, isLeft)
        else:
            get_side_boundary(root.left, res, isLeft)
        res.append(root.val)

def get_leafs(root, res):
    if not root:
        return
    
    if not root.left and not root.right:
        res.append(root.val)

    get_leafs(root.left, res)
    get_leafs(root.right, res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
root.right.left.left = Node(9)
root.right.left.right = Node(10)

print("root", root)
print("max sum path",  get_boundary(root))
    
