class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

def get_max_diameter(root):
    if not root:
        return 0
    
    max_diameter = 0
    def get_oneside_max_depth(root):
        if not root:
            return 0
        
        nonlocal max_diameter
        left_depth = get_oneside_max_depth(root.left)
        right_depth = get_oneside_max_depth(root.right)
        max_diameter = max(max_diameter, 1 + left_depth + right_depth)

        return 1 + max(left_depth, right_depth)
    
    get_oneside_max_depth(root)
    return max_diameter
    
def get_max_diameter_path(root):
    if not root:
        return []
    
    max_diameter = 0
    max_path = []

    def get_oneside_max_depth(root, path = []):
        if not root:
            return 0, path[:]
        
        nonlocal max_path, max_diameter

        path.append(root.val)
        left_depth, left_path = get_oneside_max_depth(root.left, path)
        right_depth, right_path = get_oneside_max_depth(root.right, path)
        path.pop()

        diameter = 1 + left_depth + right_depth
        if max_diameter <= diameter:
            max_diameter = diameter
            prefix_len = len(path)
            max_path = list(reversed(left_path[(prefix_len + 1):])) + right_path[prefix_len:]

        if left_depth > right_depth:
            return 1 + left_depth, left_path
        return 1 + right_depth, right_path

    get_oneside_max_depth(root)
    return max_diameter, max_path

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
print("root: ", root)
print("get_max_diameter: ", get_max_diameter(root))
print("get_max_diameter_path: ", get_max_diameter_path(root))
