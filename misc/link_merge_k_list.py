import heapq

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val
    
    def __gt__(self, other):
        return self.val > other.val

def generate_list(nums):
    prev, head = None, None
    for num in reversed(nums):
        head = Node(num, prev)
        prev = head
    return head

def merge_k_lists(lists):
    # create a heap and push each list's head
    hq = []
    for head in lists:
        if head:
            heapq.heappush(hq, head)

    # pop item from heap and append it to result list
    # and push item's next into heap

    dummy = Node(0)
    p = dummy

    while hq:
        head = heapq.heappop(hq)
        p.next = head
        p = p.next

        head = head.next
        if head:
            heapq.heappush(hq, head)

    return dummy.next


num_lists =  [ [ 3, 4, 5, 9, 11 ],
               [ 1, 2, 3, 4, 8 ],
               [ 2, 7, 9, 11, 15 ]]
lists = [ generate_list(nums) for nums in num_lists ]
print(merge_k_lists(lists))

print(Node(1) > Node(2))
print(Node(3) < Node(2))

