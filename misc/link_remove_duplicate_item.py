'''
1. Question
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->3->4->5.
Given 1->1->1->2->3, return 1->2->3.
'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

def generate_list(nums):
    pre, head = None, None
    for num in reversed(nums):
        head = Node(num, pre)
        pre = head
    return head

def remove_duplicate_items(head):
    if not head:
        return head
    
    slow, fast = head, head
    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next
        fast = fast.next
    slow.next = None

    return head

nums = [ 1, 2, 2 ]
head = generate_list(nums)
print(head)
print(remove_duplicate_items(head))