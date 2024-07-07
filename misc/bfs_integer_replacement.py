'''
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.

If n is odd, you can replace n with either n+1 or n-1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input: 8
Output: 3

Explanation:
8 ->4 ->2 ->1


Example 2:

Input:  7
Output: 4


Explanation:
7 ->8 ->4 ->2 ->1
or
7 ->6 ->3 ->2 ->1

'''

from collections import deque

def get_integer_replacement(n):
    visited = {n}
    dq = deque([(n, [n])])

    while dq:
        i, path = dq.popleft()
        if i == 1:
            print(path)
            return len(path) - 1
        
        next_integers = [ i//2 ] if i%2 == 0 else [ i-1, i+1 ]
        for j in next_integers:
            if j not in visited:
                dq.append((j, path + [j]))
                visited.add(j)

    return 0

print(get_integer_replacement(8))
print(get_integer_replacement(7))
print(get_integer_replacement(128))