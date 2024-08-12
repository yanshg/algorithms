class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
class TreeIterator:
    def __init__(self, root):
        self.curr = root
        self.stack = []

    def __iter__(self):
        return self
    
    def __next__(self):
        curr = self.curr
        while curr:
            self.stack.append(curr)
            curr = curr.left

        if self.stack:
            curr = self.stack.pop()
            val = curr.val
            self.curr = curr.right
            return val
        
        raise StopIteration

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(root)

for i in TreeIterator(root):
    print(i)
