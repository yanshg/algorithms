class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def get_max_path_sum(root):
    max_sum = float('-inf')

    def max_path_sum(root):
        nonlocal max_sum

        if not root:
            return 0
        
        left_sum = max(0, max_path_sum(root.left))
        right_sum = max(0, max_path_sum(root.right))

        max_sum = root.val + left_sum + right_sum

        return root.val + max(left_sum, right_sum)
    
    max_path_sum(root)
    return max_sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("root", root)
print("max sum path",  get_max_path_sum(root))