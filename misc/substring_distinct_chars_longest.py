'''

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

     Input: s = "abcabcbb"
     Output: 3
     Explanation: The answer is "abc", with the length of 3.

Example 2:

     Input: s = "bbbbb"
     Output: 1
     Explanation: The answer is "b", with the length of 1.

'''

from collections import defaultdict

def get_longest_distinct_chars(s: str) -> int:
    window = defaultdict(int)
    max_len = 0

    left = 0
    for right,c in enumerate(s):
        window[c] += 1

        while left<=right and window[c] > 1:
            lc = s[left]
            window[lc] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
                
s = 'abcabcbb'
assert get_longest_distinct_chars(s) == 3
