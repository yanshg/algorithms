
'''
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

    Check if the substring sources[i] occurs at index indices[i] in the original string s.
    If it does not occur, do nothing.
    Otherwise if it does occur, replace that substring with targets[i].

For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

    For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.

Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"

Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".


'''

class Solution:
    def findReplaceString(self, S, indices, sources, targets):
        modified = list(S)
        for index, source, target in zip(indices, sources, targets):
            if not S[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index+1, index + len(source)):
                    modified[i] = ""

        return "".join(modified)

solution=Solution()
print(solution.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))

