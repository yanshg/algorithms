class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def get_leaf_paths(root):

    res = []

    def dfs(root, path = [], res = []):
        if not root:
            return
        
        if not root.left and not root.right:
            res += [ path + [ root.val ]] 
            return

        path.append(root.val)
        dfs(root.left, path, res)
        dfs(root.right, path, res)
        path.pop()

    dfs(root, [], res)
    return res

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

print("root", root)
print("leaf paths: ",  get_leaf_paths(root))