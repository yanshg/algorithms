'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"

Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \\   / 
  3   1 5

Note:

There will only be '(', ')', '-' and '0'~'9' in the input string.

An empty tree is represented by "" instead of "()".

'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"

def construct_tree_from_string(s):
    stack = []

    # Notes:  the sequence is reversed after pop()
    def combine_node(stack):
        nodes = []
        while stack:
            node = stack.pop()
            if node == '(':
                break
            nodes.append(node)

        if not nodes:
            return None
        
        nodes = list(reversed(nodes))
        node = nodes[0]
        n = len(nodes)
        if n > 1:
            node.left = nodes[1]
        if n > 2:
            node.right = nodes[-1]
            
        return node      

    s = s.replace(' ', '')
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c.isdigit():
            num = int(c)
            while i+1 < n and s[i+1].isdigit():
                num = num * 10 + int(s[i+1])
                i += 1
            stack.append(Node(num))
        elif c == '(':
            stack.append('(')
        elif c == ')':
            stack.append(combine_node(stack))
        i += 1
        print(stack)

    return combine_node(stack)

s = "42(2(3)(1))(6(5))"
print(construct_tree_from_string(s))