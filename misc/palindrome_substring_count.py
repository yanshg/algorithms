'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3

Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: "aaa"
Output: 6

Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

def get_palindrome_substring_count(s: str) -> int:
    # base cases
    if not s:
        return 0
    
    n = len(s)

    # DP[i][j]: True if s[i:j+1] is palindromic else False
    #
    # 1.  True if i == j
    # 2.  True if s[i] == s[j] and j == i+1
    # 3.  DP[i+1][j-1] if s[i] == s[j]
    # 4.  False for other cases

    res = 0
    DP = [ [ False for j in range(n) ] for i in range(n) ]

    for i in reversed(range(n)):
        for j in range(i, n):
            if i == j:
                DP[i][j] = True
            elif s[i] == s[j]:
                DP[i][j] = True if j == i+1 else DP[i+1][j-1]

            if DP[i][j]:
                res += 1

    #print(DP)
    return res

s = "aaa"
assert get_palindrome_substring_count(s) == 6

s = "abc"
assert get_palindrome_substring_count(s) == 3
