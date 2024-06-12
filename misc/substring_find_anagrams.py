'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both stringssandpwill not be larger than 20,100.

The order of output does not matter.

Example 1:

Copy
Input: s: "cbaebabacd" p: "abc"

Output: [0, 6]

Explanation:

The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Copy
Input: s: "abab" p: "ab"

Output: [0, 1, 2]

Explanation:

The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

from collections import Counter, defaultdict

def find_anagram(s: str, p: str) -> list:
    res = []
    window = defaultdict(int)
    counts = Counter(p)
    lp = len(p)

    left = 0
    for right, c in enumerate(s):
        window[c] += 1
        if right >= lp - 1:
            if right > lp - 1:
                lc = s[left]
                window[lc] -= 1
                if window[lc] == 0:
                    del window[lc]
                left += 1
            if window == counts:
                res += [left]
    return res

s="cbaebabacd" 
p="abc"
assert find_anagram(s, p) == [ 0, 6 ]