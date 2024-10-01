'''
Problem Statement
Given the root of a binary tree, return the postorder traversal of its nodes’ values.

Example
Input: root = [1,null,2,3]
Output: [3,2,1]
Explanation: The postorder traversal visits the nodes in the order: left subtree, right subtree, root.


'''

# Use a stack to simulate the recursive call stack.
# Traverse the tree by pushing nodes onto the stack.
# Append node values to the result list and reverse the list at the end to get the correct postorder traversal.

# BFS with stack instead of deque

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if not root:
        return []
        
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        
    print(result)
    return result[::-1]
    
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(postorderTraversal(root))