class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

def flatten_tree_morris(root):
    curr = root
    while curr:
        if not curr.left:
            curr = curr.right
        else:
            pre = curr.left
            while pre.right:
                pre = pre.right
            pre.right = curr.right
            curr.right = curr.left
            curr.left = None
            curr = curr.right
    return root

def flatten_tree_recursion(root):
    if not root or (not root.left and not root.right):
        return root
    
    tmp_left = flatten_tree_recursion(root.left)
    tmp_right = flatten_tree_recursion(root.right)
    root.left = None
    root.right = tmp_left
    pre = root
    while pre.right:
        pre = pre.right
    pre.right = tmp_right

    return root

def flatten_tree_recursion2(root):
    if not root:
        return root
    
    if root.left:
        pre = root.left
        while pre.right:
            pre = pre.right
        pre.right = root.right
        root.right = root.left
        root.left = None

    flatten_tree_recursion2(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("before flatten: ", root)
#print("after flatten(morris): ", flatten_tree_morris(root))
print("after flatten(recursion): ", flatten_tree_recursion(root))
print("after flatten(recursion2): ", flatten_tree_recursion2(root))
