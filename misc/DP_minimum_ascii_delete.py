'''
Given two stringss1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231

Explanation:
Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403

Explanation:

Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.

All elements of each string will have an ASCII value in [97, 122].

'''

def get_minimum_ascii_delete(s1, s2):
    # base cases:
    if not s1 or not s2:
        return sum([ ord(c) for c in s1 + s2 ])
    
    # DP[i][j]: means minimum ascii deletion for s1[:i+1] and s2[:j+1]

    # if s1[i-1] == s2[j-1]:
    #    DP[i][j] = DP[i-1][j-1]
    # else:
    #    DP[i][j] = min(DP[i-1][j] + ord(s1[i-1]), DP[i][j-1] + ord(s2[j-1]))
    #
    # base case:
    #    assume the first character is '',
    #    S1 = '' + s1
    #    S2 = '' + s2
    #    f(S1, S2) = f(s1, s2)
    #    S1[i] = s1[i-1]
    #    S2[j] = s2[j-1] 
    #    
    #    DP[0][0] = 0
    #    DP[0][j] = DP[0][j-1] + ord(s2[j-1])
    #    DP[i][0] = DP[i-1][0] + ord(s1[i-1])

    # initialize DP
    m, n = len(s1), len(s2)
    DP = [ [ 0 for j in range(n+1) ] for i in range(m+1)]

    for i in range(1, m+1):
        DP[i][0] = DP[i-1][0] + ord(s1[i-1])

    for j in range(1, n+1):
        DP[0][j] = DP[0][j-1] + ord(s2[j-1])

    # calculate DP[i][j], and return DP[-1][-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                DP[i][j] = DP[i-1][j-1]
            else:
                DP[i][j] = min(DP[i-1][j] + ord(s1[i-1]), DP[i][j-1] + ord(s2[j-1]))

    return DP[-1][-1]

# Time: O(m * n)
# Space: O(m * n)

s1 = "delete"
s2 = "leet"
print(get_minimum_ascii_delete(s1, s2))