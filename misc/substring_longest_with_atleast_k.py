'''
Longest substring where all the characters appear at least K times

Given a string str and an integer K, the task is to find the length of the longest substring S such that every character in S appears at least K times.

Examples:

Input: str = “aabbba”, K = 3
Output: 6
Explanation: In substring “aabbba”, each character repeats at least k times and its length is 6.

Input: str = “ababacb”, K = 3
Output: 0
Explanation: There is no substring where each character repeats at least k times.

'''

from collections import Counter, defaultdict

def longest_substring(s: str, k: int) -> int:
    counts = Counter(s)
    valid_chars = [ c for c in counts if counts[c] >= k ]

    left, right = 0, 0
    window = defaultdict(int)
    valid = 0
    maxlen = 0

    for right, c in enumerate(s):
        if c not in valid_chars:
            while left < right:
                lc = s[left]
                if window[lc] == k:
                    valid -= 1
                window[lc] -= 1
                if window[lc] == 0:
                    del window[lc]
                left +=1
                
                if valid == len(window):
                    maxlen = max(maxlen, right - left)
                    print(s[left:right])

            window.clear()
            left = right + 1
            valid = 0
            continue

        window[c] += 1
        if window[c] == k:
            valid += 1
        if valid == len(window):
            maxlen = max(maxlen, right - left + 1)
            print("string: ", s[left: right+1])
    return maxlen

s = "aabbbca"
k = 3
print(longest_substring(s, k))

s = "cabababc"
k = 3
print(longest_substring(s, k))
