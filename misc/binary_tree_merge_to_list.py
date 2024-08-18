'''
Give you roots of 2 binary search tree, return a list include all elements in the 2 BST with ascending order
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}), ({self.right}))"

def get_generator(root):    
    stack = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.val
            curr = curr.right

def get_next_value(iter):
    try:
        return next(iter)
    except StopIteration:
        return None
    
def get_merged_list(root1, root2):
    res = []

    g1 = get_generator(root1)
    g2 = get_generator(root2)

    v1 = get_next_value(g1)
    v2 = get_next_value(g2)
    while v1 != None or v2 != None:
        if v1 != None and v2 != None:
            if v1 <= v2:
                res += [ v1 ]
                v1 = get_next_value(g1)
            else:
                res += [ v2 ]
                v2 = get_next_value(g2)
        elif v1 != None:
            res += [ v1 ]
            v1 = get_next_value(g1)
        elif v2 != None:
            res += [ v2 ]
            v2 = get_next_value(g2)

    return res

root1 = Node(2, Node(1), Node(4))
root2 = Node(1, Node(0), Node(3))
#print(list(get_values(root1)))
#print(list(get_values(root2)))
print(get_merged_list(root1, root2))