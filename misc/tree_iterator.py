class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
class TreeIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        
        root = self.stack.pop()
        self._leftmost_inorder(root.right)
        return root.val

    def _leftmost_inorder(self, root):        
        while root:
            self.stack.append(root)
            root = root.left

    def has_next(self):
        return len(self.stack) > 0

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(root)

for i in TreeIterator(root):
    print(i)
