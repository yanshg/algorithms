'''
This problem was asked by PagerDuty.

Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

1. You may decrement N to N - 1.
2. If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

'''

from collections import deque

def get_next_integers(n):
    res = [ n - 1 ]

    i = 2
    while i * i <= n:
        if n % i == 0:
            res += [ n//i ]
        i += 1

    return res

def get_smallest_steps(n):
    visited = {n}

    # need be deque( [  (n, [n])  ] )
    dq = deque([(n, [n])])

    while dq:
        i, path = dq.popleft()
        if i == 1:
            print(' -> '.join(map(str,path)))
            return len(path) - 1
        
        next_integers = get_next_integers(i)
        for ni in next_integers:
            if ni not in visited:
                visited.add(ni)
                dq.append((ni, path + [ni]))

    return -1

print(get_smallest_steps(100))
#assert get_smallest_steps(100) == 5