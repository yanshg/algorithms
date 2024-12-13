# Convert binary search tree to sorted doubly-linked list
# Define all necessary APIs and data structures

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: {self.left}, {self.right})"
   

def convert_bst_to_doubly_linked_list(root):

    prev, head = None, None

    def inorder(node):
        nonlocal prev, head

        # base case
        if not node:
            return None
        
        inorder(node.left)

        if prev:
            prev.right = node   
            node.left = prev         
        else:
            head = node
        
        prev = node

        inorder(node.right)
    
    inorder(root)
    return head
    
root = Node(1, Node(2, None, Node(5)), Node(3))
print(root)
convert_bst_to_doubly_linked_list(root)