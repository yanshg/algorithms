'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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

def split_list(head):
    # empty or only 1 node
    if not head or not head.next:
        return head, None
    
    # slow/fast pointer to get middle point
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # split the list to left and right
    left = head
    right = slow.next
    slow.next = None
    return left, right

def reverse_list(head):
    # use prev, curr, next pointer to reverse the list
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def compare_list(left, right):
    # compare node by node
    p1, p2 = left, right
    while p1 and p2:
        if p1.val != p2.val:
            return False       
        p1 = p1.next
        p2 = p2.next

    return True

def is_palindrome(head) -> bool:
    # base cases: empty or only 1 node, return True
    if not head or not head.next:
        return True
    
    # split the list to left and right
    left, right = split_list(head)
    
    # reverse the right list
    right = reverse_list(right)

    # compare if left and right list nodes have same value
    return compare_list(left, right)


nums = [ 1, 2, 2, 1]
head = generate_list(nums)
print(head)

print(is_palindrome(head))