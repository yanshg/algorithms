'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->3->4->5.
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

def partition_list(head, x):
    dummy1, dummy2 = Node(0), Node(0)
    p1, p2 = dummy1, dummy2
    p = head

    while p:
        if p.val <= x:
            # attach to list1
            p1.next = p
            p1 = p1.next
        else:
            # attach to list2
            p2.next = p
            p2 = p2.next

        p = p.next

    # connect list1 and list2
    p1.next = dummy2.next
    p2.next = None

    return dummy1.next


nums = [ 1, 5, 3, 3, 4, 2, 6]
head = generate_list(nums)
print(head)

print(partition_list(head, 3))