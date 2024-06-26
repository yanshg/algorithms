'''
This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

'''

from collections import deque

def hops_to_end(hops):
    n = len(hops)
    visited = {0}
    dq = deque([0])

    while dq:
        i = dq.popleft()
        if i == n-1:
            return True
    
        for d in range(1, hops[i]+1):
            next_hop = i + d
            if next_hop not in visited:
                dq.append(next_hop)
                visited.add(next_hop)

    return False

hops = [1, 3, 1, 2, 0, 1]
assert hops_to_end(hops)

hops = [1, 2, 1, 0, 0]
assert not hops_to_end(hops)