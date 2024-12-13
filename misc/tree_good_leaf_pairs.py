'''
1530. Number of Good Leaf Nodes Pairs

You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def get_good_leaf_pairs_count(root, distance):

    count = 0

    def dfs(root):
        if not root:
            return [0] * (distance + 1)
        
        if not root.left and not root.right:
            leaf_distances = [ 0 ] * (distance + 1)
            leaf_distances[1] = 1
            return leaf_distances
        
        left_distances = dfs(root.left)
        right_distances = dfs(root.right)

        
        
