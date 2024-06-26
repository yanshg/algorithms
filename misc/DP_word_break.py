'''

Given a non-empty strings and a dictionary wordDict containing a list of non-empty words, determine if scan be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s="leetcode",
dict=["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

def word_break(s, words):
    if not s:
        return True
    
    for i in range(len(s)):
        # i+1 is the separator index
        if s[:i+1] in words and word_break(s[i+1:], words):
            return True
    
    return False

def word_break_with_memo(s, words):
    n = len(s)

    def dfs(s, words, start = 0, memo = {}):
        if start >= n:
            return True
    
        if start in memo:
            return memo[start]

        for next_start in range(start+1, n+1):
            if s[start:next_start] in words and dfs(s, words, next_start, memo):
                memo[start] = True
                print(memo)
                return True
    
        memo[start] = False
        print("memo: ", memo)
        return False
    
    memo = {}
    res = dfs(s, words, 0, memo)
    print(memo)
    return res


def word_break_with_dp(s, words):
    #
    # S = '' + s
    #
    # DP[i]:  True if S[1:i+1](s[0:i]) is breakable else False
    #
    # DP[i]:  True if i == 0
    #         True if S[1:i+1] (s[0:i]) in words
    #         DP[j-1] if S[j:i+1] (s[j-1:i]) in words

    if not s:
        return True
    
    n = len(s)
    DP = [ False ] * (n + 1)
    DP[0] = True

    for i in range(1, n+1):
        for j in range(1, i+1):
            if DP[j-1] and s[j-1:i] in words:
                DP[i] = True
                break
    print(DP)
    return DP[-1]

s="leetcodecatsanddogsandcat"
words=["leet", "code", "and", "sand", "dog", "cats", "cat"]
print(word_break(s, words))
print(word_break_with_memo(s, words))
print(word_break_with_dp(s, words))