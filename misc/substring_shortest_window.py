'''
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is covered by W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Copy
Input:
S = "abcdebdde", T = "bde"

Output: "deb"

Explanation: 

"deb" is the answer because it occurs before "bdde" which has the same length.

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

    counts = Counter(t)
    window = defaultdict(int)
    valid = 0

    left = 0
    for right, c in enumerate(s):
        window[c] += 1
        if c in counts and window[c] == counts[c]:
            valid += 1

        while left <= right and valid == len(counts):
            # means s[left: right+1] contain all chars in t
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            # move left to make valid != len(counts)
            lc = s[left]
            if lc in counts and window[lc] == counts[lc]:
                valid -= 1
            window[lc] -= 1
            left += 1
    
    if min_len == float('inf'):
        return ''
    
    return s[min_left: min_left + min_len]

S = "abcdebdde"
T = "bde"
print(get_min_window(S, T))