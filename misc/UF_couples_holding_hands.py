'''
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being(0, 1), the second couple being(2, 3), and so on with the last couple being(2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Copy
Input: row = [0, 2, 1, 3]

Output: 1

Explanation:
We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Copy
Input: row = [3, 2, 0, 1]

Output: 0

Explanation:
All couples are already seated side by side.

Note:

len(row)is even and in the range of[4, 60].

row is guaranteed to be a permutation of 0...len(row)-1.
'''

class UF:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        
        if self.size[rootp] > self.size[rootq]:
            rootp, rootq = rootq, rootp

        self.parent[rootp] = rootq
        self.size[rootq] += self.size[rootp]
        self.count -= 1

    def get_count(self):
        return self.count
    

def get_couple_swaps(row):
    n = len(row) // 2
    uf = UF(n)
    for i in range(n):
        # union with couple ID
        c1 = row[2 * i] // 2
        c2 = row[2 * i + 1] // 2
        uf.union(c1, c2)

    # swaps = n - uf.count
    return n - uf.get_count()

row = [0, 2, 1, 3]
print(get_couple_swaps(row))

row = [3, 2, 0, 1]
print(get_couple_swaps(row))