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

from collections import deque

def is_next_mutation(gene1, gene2):
    if not gene1 or not gene2 or gene1 == gene2 or len(gene1) != len(gene2):
        return False
    
    return sum([ 1 for c1, c2 in zip(gene1, gene2) if c1 != c2 ]) == 1
    
def get_next_mutations(gene, bank):
    return [ g for g in bank if is_next_mutation(gene, g) ]
    
def get_mutations(bank, start, end):
    if not bank or not isinstance(bank, list) or end not in bank:
        return 0

    steps = 0
    visited = {start}
    dq = deque([start])

    while dq:
        for _ in range(len(dq)):
            gene = dq.popleft()
            if gene == end:
                return steps

            for next_gene in get_next_mutations(gene, bank):
                if next_gene not in visited:
                    visited.add(next_gene)
                    dq.append(next_gene)

        steps += 1
        
    return 0
        
    
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(get_mutations(bank, start, end))

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(get_mutations(bank, start, end))

