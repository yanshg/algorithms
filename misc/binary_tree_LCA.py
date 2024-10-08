from collections import deque

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

def get_parents(root, p, q):
    parents = {}

    # use bfs to get parent for p and q
    dq = deque([root])
    parents[root] = None

    while dq and (p not in parents or q not in parents):
        node = dq.popleft()

        if node.left:
            dq.append(node.left)
            parents[node.right] = node

        if node.right:
            dq.append(node.right)
            parents[node.right] = node
    
    return parents

def get_lca(root, p, q):
    if not root or not p or not q:
        return None
    
    # use bfs to get parents information for p and q
    parents = get_parents(root, p, q)
    if p not in parents or q not in parents:
        return None
    
    # get intersection of p parent list and q parent list
    while p != q:
        if p == None:
            p = q
        p = parents[p]

        if q == None:
            q = p
        q = parents[q]
    
    return p

def get_lca_binary_tree(root, p, q):
    if not root or root == p or root == q:
        return root

    left = get_lca(root.left, p, q)
    right = get_lca(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
p = root.left.left
q = root.right.right

print("root", root)
print("lca: ",  get_lca(root, p, q))    

