class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.val
            curr = curr.right

def preorder(root):
    stack = []
    curr = root
    while curr or stack:
        if curr:
            yield curr.val
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            curr = curr.right

def postorder(root):
    stack = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            if stack and curr == stack[-1]:
                curr = curr.right
            else:
                yield curr.val
                curr = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("inorder: ", list(inorder(root)))
print("preorder: ", list(preorder(root)))
print("postorder: ", list(postorder(root)))

