'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees ofeverynode never differ by more than 1.

Example:

Copy
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val}: ({self.left}) ({self.right}))"
    
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def generate_list(nums):
    prev, head = None, None
    for num in reversed(nums):
        head = ListNode(num, prev)
        prev = head
    return head

 # Helper function to find the middle of the linked list
def find_middle(start, end):
    slow = fast = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    return slow

def convert_to_bst(head, start, end):
    if not head or start == end:
        return None
    
    # first get middle element
    mid = find_middle(start, end)

    root = TreeNode(mid.val)
    root.left = convert_to_bst(head, start, mid)
    root.right = convert_to_bst(head, mid.next, end)
    
    return root

nums = [-10, -3, 0, 5, 9]
head = generate_list(nums)
print(head)

bst = convert_to_bst(head, head, None)
print(bst)