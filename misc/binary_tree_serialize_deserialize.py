
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}: ({self.left}) ({self.right})"
    
# preorder serialize

def preorder_serialize(root):
    if not root:
        return '#'
    
    return str(root.val) + "," + \
            preorder_serialize(root.left) + "," + \
            preorder_serialize(root.right)

def preorder_deserialize(s):
    sl = s.split(',')

    def helper(sl):
        if not sl:
            return None
        
        v = sl.pop(0)
        if v == '#':
            return None

        root = Node(v)
        root.left = helper(sl)
        root.right = helper(sl)

        return root

    return helper(sl)

# postorder

def postorder_serialize(root):
    if not root:
        return '#'
    
    return postorder_serialize(root.left) + ',' + \
            postorder_serialize(root.right) + ',' + \
            str(root.val)

def postorder_deserialize(s):
    sl = s.split(',')
    
    def helper(sl):
        if not sl:
            return None
        
        v = sl.pop()
        if v == '#':
            return None
        
        root = Node(v)
        root.right = helper(sl)
        root.left = helper(sl)

        return root
    
    return helper(sl)


# serialize by level

from collections import deque

def serialize_by_level(root):
    if not root:
        return '#'
    
    res = []

    dq = deque([root])
    while dq:
        node = dq.popleft()
        if not node:
            res.append('#')
            continue

        res.append(str(node.val))
        dq.append(node.left)
        dq.append(node.right)
    
    return ','.join(res)

def deserialize_by_level(s):
    sl = s.split(',')

    def helper(sl):
        if not sl or sl[0] == '#':
            return None
        
        root = Node(sl[0])
        dq = deque([root])

        i, n = 1, len(sl)
        while i < n:
            parent = dq.popleft()

            c = sl[i]
            left = None
            if c != '#':
                left = Node(c)
                dq.append(left)

            parent.left = left
            i += 1

            if i < n:
                c = sl[i]
                right = None
                if c != '#':
                    right = Node(c)
                    dq.append(right)

                parent.right = right
                i += 1

        return root
        
    return helper(sl)



root = Node(1, Node(2), Node(3))
s = preorder_serialize(root)
root = preorder_deserialize(s)
print(root)


root = Node(1, Node(2), Node(3))
s = postorder_serialize(root)
root = postorder_deserialize(s)
print(root)

root = Node(1, Node(2), Node(3))
s = serialize_by_level(root)
root = deserialize_by_level(s)
print(root)

