'''

A word square is a type of acrostic. It consists of a set of words written out in a square grid, such that the same words can be read both horizontally and vertically. 

The number of words, which is equal to the number of letters in each word, is known as the "order" of the square. For example, this is an order 5 square:

H E A R T
E M B E R
A B U S E
R E S I N
T R E N D

'''
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        def isvalid(words):
            for i in range(1,len(words)):
                for j in range(i):
                    if words[i][j] != words[j][i]:
                        return False
            return True

        def backtrack(words, l, path = [], res = []):
            if len(path) == l:
                res.append(path[:])
                return

            for word in words:
                path.append(word)
                if isvalid(path):
                    backtrack(words, l, path, res)
                path.pop()

        res = []
        backtrack(words, len(words[0]), [], res)
        return res

solution=Solution()
words=["area", "lead", "wall", "lady", "ball"]
print(solution.wordSquares(words))

words = ["abat", "baba", "atan", "atal"]
print(solution.wordSquares(words))
