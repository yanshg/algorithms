'''
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.

The column number n should always be an odd number.

The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.

Each unused space should contain an empty string"".

Print the subtrees following the same rules.

Example 1:

Copy
Input:

     1
    /
   2

Output:

[["", "1", ""],
 ["2", "", ""]]
Example 2:

Copy
Input:

     1
    / \
   2   3
    \
     4

Output:

[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:

Copy
Input:

      1
     / \
    2   5
   / 
  3 
 / 
4 

Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note:The height of binary tree is in the range of [1, 10].

'''

class Node:
    def __init__(self, val , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def get_height(root):
    # base case
    if not root:
        return 0
    
    return 1 + max(get_height(root.left), get_height(root.right))

def print_tree_hierarchy(root):
    rows = get_height(root)
    cols = (1 << rows) - 1

    matrix = [ [ "" for j in range(cols) ] for i in range(rows) ]

    def place_position_in_matrix(root, row, left, right):
        if not root:
            return
        
        mid = left + (right - left)// 2
        matrix[row][mid] = str(root.val)

        place_position_in_matrix(root.left, row + 1, left, mid - 1)
        place_position_in_matrix(root.right, row + 1, mid + 1, right)

    place_position_in_matrix(root, 0, 0, cols - 1)
    print(matrix)


'''
      1
     / \
    2   5
   / 
  3 
 / 
4 
'''

root = Node(1, Node(2, Node(3, Node(4))), Node(5))
print_tree_hierarchy(root)