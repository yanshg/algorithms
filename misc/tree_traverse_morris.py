class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    curr = root
    while curr:
        if not curr.left:
            yield curr.val
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            elif pre.right == curr:
                pre.right = None
                yield curr.val
                curr = curr.right

def preorder(root):
    curr = root
    while curr:
        if not curr.left:
            yield curr.val
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if pre.right == None:
                pre.right = curr
                yield curr.val
                curr = curr.left
            elif pre.right == curr:
                pre.right = None
                curr = curr.right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("inorder: ", list(inorder(root)))
print("preorder: ", list(preorder(root)))

