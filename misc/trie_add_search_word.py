'''
Design a data structure that supports the following two operations:

Copy
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only lettersa-zor.. A.means it can represent any one letter.

For example:

Copy
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''

class Trie:
    def __init__(self):
        self.trie = {}

    def __repr__(self):
        return f"{self.trie}"
    
    def addWord(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['is_word'] = True

    def _search_trie(self, trie, s, path = [], res = []):
        if not trie:
            return
        
        if not s:
            if trie['is_word'] and path:
                res += [ ''.join(path) ]
            return
        
        c = s[0]
        for ct in trie:
            if c == '.' or c == ct:
                path.append(ct)
                self._search_trie(trie[ct], s[1:], path, res)
                path.pop()

    def search(self, word):
        res = []
        self._search_trie(self.trie, word, [], res)
        return bool(res)

trie = Trie()
trie.addWord('bad')
trie.addWord('dad')
trie.addWord('mad')

print("trie: ", trie)

assert not trie.search('pad')
assert trie.search('bad')
assert trie.search('.ad')
assert trie.search('b..')