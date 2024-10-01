"""

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""


# use Dynamic programming

# DP[i][j] means shortest palindrome made by s[i:j+1]

# DP[i][j]:  
#        s[i]    if i == j
#        s[i] + DP[i+1][j-1] + s[i]     if s[i] == s[j]
#        s[i] + DP[i+1][j] + s[i]  or s[j] + DP[i][j-1] + s[j] if s[i] != s[j]

# return DP[0][l-1]

def get_shortest_palindrome_string(s: str) -> str:
    l = len(s)
    DP = [ [ '' for j in range(l) ] for i in range(l) ]
    for i in reversed(range(l)):
        for j in range(i, l):
            if i == j:
                DP[i][j] = s[i]
            elif s[i] == s[j]:
                DP[i][j] = s[i] + DP[i+1][j-1] + s[i]
            else:
                s1 = s[i] + DP[i+1][j] + s[i]
                s2 = s[j] + DP[i][j-1] + s[j]
                l1, l2 = len(s1), len(s2)
                if l1 < l2 or (l1 == l2 and s1 < s2):
                    DP[i][j] = s1
                else:
                    DP[i][j] = s2
    return DP[0][l-1]

assert get_shortest_palindrome_string("race") == "ecarace"
assert get_shortest_palindrome_string("google") == "elgoogle"