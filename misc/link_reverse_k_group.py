'''
reverse every k nodes in a list 
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

def reverse_k_group(head, k):
    # base cases
    if not head or k <= 1:
        return head
    
    # move k nodes to get next break point
    next_start = head
    for i in range(k):
        if not next_start:
            # not enough k nodes, directly return
            return head
        next_start = next_start.next
    
    # reverse the k nodes between head and next_start
    prev, curr = None, head
    while curr != next_start:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    # reverse the remaining nodes with recursion
    head.next = reverse_k_group(next_start, k)
    return prev

nums = [ 1, 2, 3, 4, 5, 6, 7 ]
head = generate_list(nums)
print(head)
print(reverse_k_group(head,3))