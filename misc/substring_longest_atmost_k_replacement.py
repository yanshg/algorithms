'''

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Copy
Input: s = "ABAB", k = 2

Output: 4

Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Copy
Input: s = "AABABBA", k = 1

Output: 4

Explanation: 
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

from collections import defaultdict
def longest_substring_with_k_replaces(s: str, k: int)->int:
    window = defaultdict(int)
    left = 0
    max_count = 0
    max_len = 0
    for right, c in enumerate(s):
        window[c] += 1

        max_count = max(window.values())
        if right - left + 1 - max_count > k:
            # move left
            lc = s[left]
            window[lc] -= 1
            if window[lc] == 0:
                del window[lc]
            left += 1
            
        max_len = max( max_len, right - left + 1 )
        print(max_len, "string:", s[left:right+1])
    return max_len


s = "AACBABBA"
k = 1
print(longest_substring_with_k_replaces(s,k))

