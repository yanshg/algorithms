class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    def __repr__(self):
        return f"({self.val}: ({self.children}))"       

def n_ary_oneside_max_depth_orig(root):
    if not root:
        return 0
    
    depths = [ n_ary_oneside_max_depth_orig(child) for child in root.children ]
    max_depth = max(depths) if depths else 0
    return 1 + max_depth

def n_ary_max_diameter(root):
    if not root:
        return 0
    
    max_diameter = 0
    def n_ary_oneside_max_depth(root):
        if not root:
            return 0
        
        nonlocal max_diameter

        first_max_depth = 0
        second_max_depth = 0
        
        for child in root.children:
            depth = n_ary_oneside_max_depth(child)
            if depth > first_max_depth:               
                second_max_depth = first_max_depth
                first_max_depth = depth
            elif depth > second_max_depth:
                second_max_depth = depth
        
        #print("first_depth:", first_max_depth, "second_depth", second_max_depth)
        max_diameter = max(max_diameter, 1 + first_max_depth + second_max_depth)

        return 1 + first_max_depth

    n_ary_oneside_max_depth(root)
    return max_diameter


def n_ary_max_diameter_path(root):
    if not root:
        return []
    
    max_diameter = 0
    max_path = []

    def n_ary_oneside_max_depth_path(root, path = []):
        #print("\n")
        #print(root, 'path: ', path)
        if not root:
            return 0, path[:]
        
        nonlocal max_diameter, max_path

        path.append(root.val)
        
        first_max_depth = 0

        # path: absolute path from root to the current node
        # in case children is empty
        first_max_path = path[:]

        second_max_depth = 0
        second_max_path = []
        
        for child in root.children:
            depth, child_path = n_ary_oneside_max_depth_path(child, path)
            #print('child depth: ', depth, 'child path: ', child_path)
            if depth > first_max_depth:               
                second_max_depth = first_max_depth
                second_max_path = first_max_path
                first_max_depth = depth
                first_max_path = child_path
            elif depth > second_max_depth:
                second_max_depth = depth
                second_max_path = child_path
        path.pop()
        
        max_diameter = 1 + first_max_depth + second_max_depth
        l = len(path)
        max_path = list(reversed(first_max_path[(l+1):])) + second_max_path[:]
        return 1 + first_max_depth, first_max_path

    n_ary_oneside_max_depth_path(root, [])
    print("max_path: ", max_path)
    return max_diameter

root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
root.children = [ node1, node2, node3 ]
node2.children = [ node4 ]
node4.children = [ node5 ]
print("depth: ", n_ary_oneside_max_depth_orig(root))

print(n_ary_max_diameter(root))

print(n_ary_max_diameter_path(root))
