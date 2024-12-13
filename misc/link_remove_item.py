'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val= 6
Return: 1 --> 2 --> 3 --> 4 --> 5

'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def remove_item(head, val) -> Node:
    if not head:
        return head
    
    dummy = Node(0, head)
    prev, curr = dummy, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return dummy.next

def generate_list(nums):
    prev, head = None, None
    for num in reversed(nums):
        head = Node(num, prev)
        prev = head
    return head

nums = [ 1, 3, 5, 6, 7, 8 ]
head = generate_list(nums)
print(head)

print(remove_item(head, 6))