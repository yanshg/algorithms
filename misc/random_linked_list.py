'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

'''

import random

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def generate_list(nums):
    head, next = None, None
    for n in reversed(nums):
        head = Node(n, next)
        next = head
    return head

def get_random(head):
    i = 0
    p = head
    res = head.val

    while p:
        r = random.randint(0, i)
        if r == 0:
           res = p.val
        
        i += 1
        p = p.next
    
    return res

nums = [ 1, 3, 4, 5 ]
head = generate_list(nums)
print(head)
print(get_random(head))