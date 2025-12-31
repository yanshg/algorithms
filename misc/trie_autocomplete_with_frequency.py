
END_FLAG = '#'
class Trie():

    def __init__(self):
        self._trie = {}

    def __repr__(self):
        return str(self._trie)
    
    def insert(self, s):
        trie = self._trie
        for c in s:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie[END_FLAG] = {}
    
    def _elements(self, trie):
        res = []
        for c in trie:
            if c == END_FLAG:
                res += ['']
            else:
                res += [ c + elem for elem in self._elements(trie[c]) ]
        return res

    def find(self, prefix):
        res = []
        trie = self._trie

        for c in prefix:
            if c not in trie:
                return None
            trie = trie[c]

        return { prefix + elem for elem in self._elements(trie) }


trie = Trie()
trie.insert('hello')
trie.insert('hell')
trie.insert('world')
print(trie)
