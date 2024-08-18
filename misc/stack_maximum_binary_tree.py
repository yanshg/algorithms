'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.

The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.

The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example:

Input:
 [3,2,1,6,0,5]

Output:
 return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

'''

# Monotone Stack

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right})"
    
# pop out items which less than current.
def get_maximum_binary_tree(nums):
    if not nums:
        return None
    
    stack = []
    for num in nums:
        curr_node = Node(num)
        while stack and stack[-1].val < num:
            node = stack.pop()
            curr_node.left = node
        if stack:
            stack[-1].right = curr_node
        stack.append(curr_node)

    return stack[0]

nums = [3,2,1,6,0,5]
print(get_maximum_binary_tree(nums))

