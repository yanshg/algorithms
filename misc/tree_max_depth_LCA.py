class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

def get_max_depth_LCA(root):

    max_depth_lca = None

    def get_max_depth(root):
        if not root:
            return 0
    
        # leaf node not possible be LCA
        if not root.left and not root.right:
            return 1
        
        nonlocal max_depth_lca

        left_depth = get_max_depth(root.left)
        right_depth = get_max_depth(root.right)
        
        # LCA node should be left_depth == right_depth
        if left_depth == right_depth:
            max_depth_lca = root
       
        return 1 + max(left_depth, right_depth)

    get_max_depth(root)
    return max_depth_lca
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.right.left = Node(6)
#root.right.right = Node(7)

print("root", root)
print("lca: ",  get_max_depth_LCA(root))