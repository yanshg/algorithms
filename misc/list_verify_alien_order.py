'''
Problem Statement
In an alien language, they use English lowercase letters, but possibly in a different order. Given a sequence of words written in the alien language and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example

Input:
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

Output: true

'''
def isAlienSorted(words, order):
    order_index = {c: i for i, c in enumerate(order)}
    
    def is_sorted(word1, word2):
        for c1, c2 in zip(word1, word2):
            if order_index[c1] < order_index[c2]:
                return True
            elif order_index[c1] > order_index[c2]:
                return False
        return len(word1) <= len(word2)
    
    for w1, w2 in zip(words, words[1:]):
        print(w1, w2)
        if not is_sorted(w1, w2):
            return False
    return True

words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert isAlienSorted(words, order)