'''
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components inG, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input:

head: 0->1->2->3
G = [0, 1, 3]

Output: 2

Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Copy
Input:
head: 0->1->2->3->4
G = [0, 3, 1, 4]

Output: 2

Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If Nis the length of the linked list given by head, 1 <= N <= 10000.

The value of each node in the linked list will be in the range[0, N - 1].

1 <= G.length <= 10000.

Gis a subset of all values in the linked list.
'''

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

def get_connected_components(head, G):
    # base cases
    if not head or not G:
        return 0

    vset = set(G)

    res = 0
    p = head
    while p:
        # traverse link
        # get to the end of connected components and do res+1
        if (p.val in vset) and (p.next == None or p.next.val not in vset):
            res += 1
        p = p.next

    return res

nums = list(range(4))
head = generate_list(nums)
print(head)

G = [ 0, 3, 1, 4 ]
print(get_connected_components(head, G))