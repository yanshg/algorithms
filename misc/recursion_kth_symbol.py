'''
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

N will be an integer in the range [1, 30].

K will be an integer in the range [1, 2^(N-1)].
'''

'''
Index:

Row 1:             1
Row 2:            1  2
Row 3:         1  2  3  4
Row 4:    1  2  3  4  5  6  7  8


for (N, K) symbol, its parent:  (N-1, (K+1)//2)

'''

def get_kth_symbol(N, K):
    if N == 1:
        return 0
    
    # get the symbol of its parent
    symbol = get_kth_symbol(N-1, (K+1)//2)

    if K % 2 == 1:
        return symbol
    
    return 1 - symbol

assert get_kth_symbol(1, 1) == 0
assert get_kth_symbol(2, 1) == 0
assert get_kth_symbol(4, 4) == 0

