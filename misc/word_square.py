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

        def backtrack(candidate, length, words_set, output):
            if len(candidate) == length:
                output.append(candidate[:])
                return

            for word in words_set:
                candidate.append(word)
                if isvalid(candidate):
                    backtrack(candidate, length, words_set, output)
                candidate.pop()


        words_set = set(words)
        length = len(words[0])
        output = []
        candidate = []
        backtrack(candidate, length, words_set, output)
        return output

solution=Solution()
words=["area","lead","wall","lady","ball"]
output=solution.wordSquares(words)
print(output)

words = ["abat","baba","atan","atal"]
output=solution.wordSquares(words)
print(output)
