'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
'''

# Do not need visited

from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, edges):
        self.adj = defaultdict(list)
        for u, v, p in edges:
            self.adj[u] += [[v, p]]

def build_graph(edges):
    graph = defaultdict(list)
    for u, v, p in edges:
        graph[u].append((v, p))
    return graph

def get_max_prob_heap(graph, start, end):
    probs = defaultdict(float)
    probs[start] = 1
    hq = [ (1, start)]
    
    while hq:
        print(hq)
        prob, node = heapq.heappop(hq)
        #if node == end:
        #    return prob
        
        if prob < probs[node]:
            continue

        for neigh, neigh_prob in graph[node]:
            print(f"node: {node},  neigh: {neigh}, prob: {neigh_prob}")
            new_prob = prob * neigh_prob
            print(f"prob: {prob}, new_prob: {new_prob}")
            if new_prob > probs[neigh]:
                probs[neigh] = new_prob
                heapq.heappush(hq, (new_prob, neigh))

    return probs[end]


def get_max_prob_bfs(graph, start, end):
    probs = defaultdict(float)
    probs[start] = 1
    dq = deque([ (1, start) ])
    visited = set()
    
    while dq:
        print(dq)
        prob, node = dq.popleft()
        if prob < probs[node]:
            continue

        for neigh, neigh_prob in graph[node]:
            new_prob = prob * neigh_prob
            if new_prob > probs[neigh]:
                probs[neigh] = new_prob
                dq.append((new_prob, neigh))

    return probs[end]

edges = [[0, 1, 0.5], [1, 2, 0.5], [0, 2, 0.3]]
start = 0
end = 2
graph = build_graph(edges)
#print(get_max_prob_heap(graph, start, end))
print(get_max_prob_bfs(graph, start, end))