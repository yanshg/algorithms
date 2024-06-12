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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("root", root)
print("leaf paths: ",  get_leaf_paths(root))