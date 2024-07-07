'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input:

 Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output:
 "1(2(4))(3)"

Explanation:
 Originally it needs to be "1(2(4)())(3()())", 


but you need to omit all the unnecessary empty parenthesis pairs. 

And it will be "1(2(4))(3)".

Example 2:

Input:

 Binary tree: [1,2,3,null,4]

       1
     /   \
    2     3
     \
      4 

Output:
 "1(2()(4))(3)"

Explanation:

Almost the same as the first example, 

except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
def construct_binary_tree_to_string(root):
    # base case
    if not root:
        return ""
    
    left = construct_binary_tree_to_string(root.left)
    right = construct_binary_tree_to_string(root.right)

    if right:
        return f"{root.val}({left})({right})"
    elif left:
        return f"{root.val}({left})"
    
    return f"{root.val}"

'''
       1
     /   \
    2     3
   /    
  4     

  result:  1(2(4))(3)
'''
root = Node(1, Node(2, Node(4)), Node(3))
print(construct_binary_tree_to_string(root))

'''
       1
     /   \
    2     3
     \
      4 
    
   result:  1(2()(4))(3)
'''
root = Node(1, Node(2, None, Node(4)), Node(3))
print(construct_binary_tree_to_string(root))
