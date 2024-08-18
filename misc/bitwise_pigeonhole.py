'''
This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

'''

# elements:  1, 2, 3, 4, 5, 6, 7, 3
# index:     1, 2, 3, 4, 5, 6, 7, 8

# Solution:  XOR element and it's index

def find_duplicated(elems):
    n = len(elems)

    x = 0
    for i, e in enumerate(elems):
        x ^= (i+1) ^ e
    
    return x ^ n

elems = [ 1, 2, 3, 3, 4, 5, 6, 7 ]
print(find_duplicated(elems))