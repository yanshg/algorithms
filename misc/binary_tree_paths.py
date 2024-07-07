'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def get_root_to_leaf_paths(root):
    res = []

    def get_paths(root, path = [], res = []):
        # base cases
        if not root:
            return
        
        if not root.left and not root.right:
            res.append('->'.join(map(str, path + [ root.val ])))
            return
        
        path.append(root.val)
        get_paths(root.left, path, res)
        get_paths(root.right, path, res)
        path.pop()

    get_paths(root, [], res)
    return res

root = Node(1, Node(2, None, Node(5)), Node(3))
print(root)
print(get_root_to_leaf_paths(root))