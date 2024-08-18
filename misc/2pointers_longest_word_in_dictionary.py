'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Copy
Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]


Output: "apple"
Example 2:

Copy
Input: s = "abpcplea", d = ["a","b","c"]

Output: "a"
Note:

All the strings in the input will only contain lower-case letters.

The size of the dictionary won't exceed 1,000.

The length of all the strings in the input won't exceed 1,000.

'''

def is_subsequence(word, s):
    if not word or not s:
        return False
    
    lw, ls = len(word), len(s)
    if lw > ls:
        return False
    
    i, j = 0, 0
    while i < lw and j < ls:
        if word[i] == s[j]:
            i += 1   
        j += 1

        if i == lw:
            return True
    
    return False

def get_longest_word(s, d):
    res = ''
    for w in d:
        if is_subsequence(w, s):
            lw, lr = len(w), len(res)

            # use comparison operators like '<', '>', '==', '<=', and '>='. 
            # which comparing two strings based on their alphabetical order
            if lw > lr or (lw == lr and w < res):
                res = w
    
    return res

s = "abpcplea"
d = ["ale","apple","monkey","plea"] 
print(get_longest_word(s, d))

s = "abpcplea"
d = ["b","a","c"]
print(get_longest_word(s, d))


