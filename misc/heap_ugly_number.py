'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first10ugly numbers.

Note that1is typically treated as an ugly number, and n does not exceed 1690.

'''

import heapq

def get_ugly_number(n):
    hq = [ 1 ]
    i = 0
    while hq:
        k = heapq.heappop(hq)
        if i == n:
            return k
        
        for factor in [ 2, 3, 5 ]:
            heapq.heappush(hq, k * factor)
        i += 1

assert get_ugly_number(0) == 1
assert get_ugly_number(1) == 2
assert get_ugly_number(5) == 6