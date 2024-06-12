# merge sort

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
def generate_list(nums):
    # generate the list
    prev, head = None, None
    for num in reversed(nums):
        head = Node(num, prev)
        prev = head
    return head


def split_list(head):
    # base cases:  empty or only 1 node 
    if not head or not head.next:
        return head, None
    
    # slow/fast pointers to get middle node and split
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # split to left and right lists
    left = head
    right = slow.next
    slow.next = None

    return left, right

def merge_list(left, right):
    # use dummy node for the head of a new list
    dummy = Node(0)

    # p1: pointer of left list
    # p2: pointer of right list
    # p:  pointer of merged list
    p1, p2, p = left, right, dummy
    while p1 and p2:
        if p1.val <= p2.val:
            # attach p1 to merged list and move p1 pointer
            p.next = p1
            p1 = p1.next
        else:
            # p2 <= p1, attach p2 to merged list and move p2 pointer
            p.next = p2
            p2 = p2.next
        p = p.next
    
    p.next = p1 if p1 else p2
    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    left, right = split_list(head)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_list(left, right)

nums = [ 9, 3, 5, 8, 4, 2, 1 ]
head = generate_list(nums)
print(head)
print(merge_sort(head))