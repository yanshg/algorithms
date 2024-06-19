'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result. If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

S will consist of lowercase letters and have length in range [1, 500].
'''

from collections import Counter
import heapq

def reorganize_string(s):
    if not s:
        return ""
    
    res = ""
    l = len(s)
    counts = Counter(s)

    # push characters with count in Max Heap
    hq = []
    for c, count in counts.items():
        if count > (l+1)//2:
            return ""
        heapq.heappush(hq, (-count, c))
    
    while len(hq) > 1:
        # pop 2 characters every time
        count1, c1 = heapq.heappop(hq)
        count2, c2 = heapq.heappop(hq)
        
        last = res[-1] if res else ""
        if c1 == last:
            c1, c2 = c2, c1

        res += c1 + c2

        # -count1 - 1 > 0
        if count1 + 1 < 0:
            # -(-count1 - 1) = count1 + 1
            heapq.heappush(hq, (count1 + 1, c1))

        if count2 + 1 < 0:
            heapq.heappush(hq, (count2 + 1, c2))
    
    if hq:
        count1, c1 = heapq.heappop(hq)
        if -count1 > 1:
            return ""
            
        res += c1

    return res

s = "aab"
print(reorganize_string(s))
#assert reorganize_string(s) == "aba"

s = "aaab"
print(reorganize_string(s))
#assert reorganize_string(s) == ""

s = "aaabbccc"
print(reorganize_string(s))

