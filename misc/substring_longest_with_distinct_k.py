'''
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s =“eceba”,

T is "ece" which its length is 3.
'''

from collections import defaultdict

def longest_substring(s:str, distinct_count:int) -> int:
    if not s:
        return 0

    maxlen = float('-inf')

    # count characters in window between left and right pointer
    window = defaultdict(int)

    left = 0
    for right, c in enumerate(s):
        window[c] += 1

        while left <= right and len(window) > distinct_count:
            # move left
            lc = s[left]
            window[lc] -= 1
            if window[lc] == 0:
                del window[lc]
            left += 1
        
        print(s[left: right+1])
        maxlen = max(maxlen, right - left + 1)

    return maxlen

s='eceba'
print(longest_substring(s, 2))
            
