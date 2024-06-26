'''
Given a non-empty strings and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s="catsanddog",
dict= ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

'''

def word_break_path(s, words):
    def dfs(s, words, path=[], res = []):
        if not s:
            if path:
                res += [ path[:] ]
            return
        
        for i in range(len(s)):
            if s[:i+1] in words:           
                path.append(s[:i+1])
                dfs(s[i+1:], words, path, res)
                path.pop()
        
    res = []
    dfs(s, words, [], res)
    print(res)
    return [ ' '.join(path) for path in res ]

def word_break_path_with_memo(s, words):
    n = len(s)

    def dfs(s, words, start = 0, memo = {}, path=[], res = [], local_path = [], local_res = []):
        if start >= n:
            if path:
                res += [ path[:] ]
                local_res += [ local_path[:] ]
                print("local_path: ", local_path, "local_res: ", local_res)
                print("memo: ", memo)
            return
        
        if start in memo:
            for new_path in memo[start]:
                res += [ path + new_path ]
                return
        
        local_res1 = []
        local_path1 = []

        for next_start in range(start+1, n+1):
            if s[start:next_start] in words:           
                path.append(s[start:next_start])
                local_path1.append(s[start:next_start])
                dfs(s, words, next_start, memo, path, res, local_path1, local_res1)
                path.pop()
                local_path1.pop()
        
        memo[start] = local_res1[:]
        print(memo)
        
    res = []
    memo = {}
    dfs(s, words, 0, memo, [], res, [], [])
    print("memo: ", memo)
    return [ ' '.join(path) for path in res ]


s = "catsanddogcatsanddogcatdog"
words = ["cat", "cats", "and", "sand", "dog"]
#res = ["cats and dog", "cat sand dog"]
#print(word_break_path(s, words))

print(word_break_path_with_memo(s, words))
#assert word_break_path(s, words) == res

    

    