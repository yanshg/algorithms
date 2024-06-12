'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:

Copy
Given 1->2->3->4->5->NULL and k= 2,

return 4->5->1->2->3->NULL.
'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def generate_list(nums):
    prev, head = None, None
    for num in reversed(nums):
        head = Node(num, prev)
        prev = head
    return head

def rotate_list(head, k):
    # base case
    if not head or k == 0:
        return head
    
    # first check if k < len(list),
    l = 1
    curr = head
    while curr.next:
        curr = curr.next
        l += 1

    if k == l:
        return head
    
    # connect the tail to head
    curr.next = head
  
    # move pointer right k place
    k = k % l 
    curr = head
    for i in range(k):
        curr = curr.next

    # split the link
    head = curr.next
    curr.next = None

    return head

nums = [ 1, 2, 3, 4, 5 ]
head = generate_list(nums)
print(head)
print(rotate_list(head, 2))


    