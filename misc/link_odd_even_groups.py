'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def generate_link(nums):
    prev, head = None, None
    for num in reversed(nums):
        head = Node(num, prev)
        prev = head
    return head

def group_odd_even_nodes(head):
    odd_head, even_head = Node(1), Node(2)    
    p1, p2 = odd_head, even_head

    curr = head
    state = 0
    while curr:
        if state == 0:
            p1.next = curr
            p1 = curr
        else:
            p2.next = curr
            p2 = curr

        state = 1 - state
        curr = curr.next

    p1.next = even_head.next
    p2.next = None

    return odd_head.next


nums = [ 1, 2, 3, 4, 5 ]
head = generate_link(nums)
print(group_odd_even_nodes(head))