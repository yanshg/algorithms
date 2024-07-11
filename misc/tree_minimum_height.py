'''
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected,[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4,edges = For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from0ton - 1. You will be given the number n and a list of undirected edges(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected,[0, 1]is the same as[1, 0]and thus will not appear together in edges.

Example 1:

Given n = 4,edges = [[1, 0], [1, 2], [1, 3]]

Copy
        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6,edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

Copy
     0  1  2
      \\ | /
        3
        |
        4
        |
        5
return [3, 4]
'''

from collections import deque

def build_graph(n, edges):
    graph = {}
    for i in range(n):
        graph[i] = set()

    for i, j in edges:
        if i < n and j < n:
            graph[i].add(j)
            graph[j].add(i)

    return graph

def get_minimum_height_tree_roots(graph):
    # first get leaf nodes
    dq = deque([ i for i in graph if len(graph[i]) == 1 ])
    
    # remove leaf nodes from graph level by level, until only 1 or 2 nodes left.
    while dq and len(graph) > 2:
        for _ in range(len(dq)):
            i = dq.popleft()
            del graph[i]

            for j in graph:
                if i in graph[j]:
                    graph[j].discard(i)
                    if len(graph[j]) == 1:
                        dq.append(j)

    return list(graph.keys())

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
graph = build_graph(n, edges)
print(graph)
print(get_minimum_height_tree_roots(graph))

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
graph = build_graph(n, edges)
print(graph)
print(get_minimum_height_tree_roots(graph))
