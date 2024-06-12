'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def get_cycle_point(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if slow != fast:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
