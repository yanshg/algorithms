'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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

def remove_duplicates(head):
    if not head:
        return head
    
    dummy = Node(0, head)
    prev = dummy
    slow, fast = head, head
    while fast:
        if slow.val != fast.val:
            if slow.next == fast:
                # not duplicate
                prev = slow
            else:
                # duplicates
                prev.next = fast
            slow = fast

        fast = fast.next

    return dummy.next

nums = [ 1, 1, 1, 2, 3]
head = generate_list(nums)
print(remove_duplicates(head))

nums = [ 1, 2, 3, 3, 4, 4, 5]
head = generate_list(nums)
print(remove_duplicates(head))
