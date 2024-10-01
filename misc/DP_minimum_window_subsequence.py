'''
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"

Output: "bcde"

Explanation: 

"bcde" is the answer because it occurs before "bdde" which has the same length.

"deb" is not a smaller window because the elements of T in the window must occur in order.

Note:

All the strings in the input will only contain lowercase letters. The length ofSwill be in the range[1, 20000].

The length of T will be in the range[1, 100].
'''

from collections import Counter, defaultdict

def get_min_window(s, t):
    # base cases:
    if not s or not t:
        return ''
    
    min_left, min_len = 0, float('inf')
    j = 0
    for i, c in enumerate(s):
        if c == t[j]:
            j += 1
            if j == 1:
                min_left = i
            elif j == len(t):
                min_len = i - min_left + 1
                break
                
    if min_len == float('inf'):
        return ''
    
    return s[min_left: min_left + min_len]

S = "abcdebdde"
T = "bde"
print(get_min_window(S, T))