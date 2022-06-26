'''
R       100GB                   R
    R1      100GB                   Raid5
c       c   100GB each          c  c   c c

      R        100GB
    Raid1
    r1  r1
   c c  c c


class Node(object):
    def __init__(self, type, addSpace=0, children=[]):
        self.children = [Nodes]
        self.addSpace = addSpace
        self.type = type
'''

    def getRaidFactor(raidType):
        pass

    def fillAddSpace(root):

        pass


#question: given an object tree struct, fill in the addSpace of each node.
#simplified: given a binary tree, copy value of root to every node.
#raid5: 100, 1.333, 4, (100 * 1.333 / 4), addSpace * raidFact(parentNode) / len(children)

def fillAddSpace(root): #recursion

    if not root:  return

    for child in root.children:
        child.addSpace = (root.addSpace * getRaidFactor(root.type)) / len(root.children)

    for child in root.children:
        fillAddSpace(child)

    return


from collections import deque

'''
root
r5
r1 r1 r1 r1
cc cc cc cc
'''
'''depth first with iteration'''

def fillAddSpace_stack(root): # level traverse

    dq = deque([root])
    while dq:
        node = dq.popleft()

        for child in node.children:
            child.addSpace = (node.addSpace * getRaidFactor(node.type)) / len(node.children)
            dq.append(child)
    return


def dfs ( root, visited=set()):

    visited.add(root)
    for child in root.children:
        if child not in visited:
            child.addSpace = (node.addSpace * getRaidFactor(node.type)) / len(node.children)
            dfs (child, visited)




