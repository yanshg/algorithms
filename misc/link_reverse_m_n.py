'''

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m= 2 and n= 4,

return 1->4->3->2->5->NULL.

Note:
Given m,n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def reverse_list(head, m, n):
    if not head:
        return head
    
    dummy = Node(0, head)
    prev = dummy
    for i in range(m-1):
        if prev:
            prev = prev.next  

    if not prev or not prev.next or not prev.next.next:
        return head
    
    # reverse nodes after m
    node_m = prev
    curr = prev.next
    for i in range(m-1, n):
        if curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        else:
            break

    if node_m.next:
        node_m.next.next = curr
        node_m.next = prev

    return dummy.next

def reverse_list1(head, m, n):
    if not head:
        return head
    
    # First get prev node of m
    dummy = Node(0, head)
    prev = dummy
    for i in range(m-1):
        if prev:
            prev = prev.next           
    
    if not prev or not prev.next or not prev.next.next:
        return head
    
    # reverse nodes after m
    curr = prev.next
    next = curr.next
    for i in range(m-1, n-1):
        if next:
            curr.next = next.next
            next.next = prev.next
            prev.next = next
            next = curr.next

    return dummy.next

def generate_list(nums):
    prev, head = None, None
    for num in reversed(nums):
        head = Node(num, prev)
        prev = head
    return head

nums = [1, 2, 3, 4, 5]
head = generate_list(nums)
print(head)

head = reverse_list1(head, 2, 4)
print(head)