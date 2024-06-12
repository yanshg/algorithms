# Union Find

class UF:
    def __init__(self, n):
        self.capacity = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)

        # if already union-ed before
        if rootp == rootq:
            return
        
        if self.size[rootp] > self.size[rootq]:
            rootp, rootq = rootq, rootp

        # smaller tree should be under bigger tree
        self.parent[rootp] = rootq
        self.size[rootq] += self.size[rootp]
        self.count -= 1

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq
    
    def get_count(self):
        return self.count
    
uf = UF(10)
uf.union(1, 2)
print(uf.connected(1, 2))
print(uf.get_count())