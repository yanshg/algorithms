'''
A gene string can be represented by an 8-character long string, with choices from "A","C","G","T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT"->"AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.

If multiple mutations are needed, all mutations during in the sequence must be valid.

You may assume start and end string is not the same.

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
'''

from collections import deque, defaultdict

def is_next_mutation(gene1, gene2):
    if not gene1 or not gene2 or len(gene1) != len(gene2):
        return False
    
    diff = sum([ int(c1 != c2) for c1, c2 in zip(gene1, gene2) ])
    return diff == 1
    
def build_graph(genes):
    graph = defaultdict(list)

    n = len(genes)
    for i in range(n-1):
        for j in range(i+1, n):
            if is_next_mutation(genes[i], genes[j]):
                graph[genes[i]] += [ genes[j] ]
                graph[genes[j]] += [ genes[i] ]

    return graph

def get_mutations(bank, start, end):
    graph = build_graph(bank + [ start ])
    print(graph)

    visited = {start}
    dq = deque([(start, [start])])

    while dq:
        gene, path = dq.popleft()
        if gene == end:
            print(path)
            return len(path) - 1
        
        for next_gene in graph[gene]:
            if next_gene not in visited:
                dq.append((next_gene, path + [next_gene]))
                visited.add(next_gene)
    
    return 0
        
    
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(get_mutations(bank, start, end))

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(get_mutations(bank, start, end))

