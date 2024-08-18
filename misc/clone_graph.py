'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely. We use#as a separator for each node, and,as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.

Second node is labeled as 1. Connect node 1 to node 2.

Third node is labeled as 2. Connect node 2 to node 2(itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

'''

from collections import defaultdict

class Graph:
    def __init__(self, serialized_str):
        self.graph = defaultdict(list)
        self.build(serialized_str)

    def __repr__(self):
        pass

    def build(self, serialized_str):
        nodes = list(map(lambda s: s.split(','), serialized_str.split('#')))
        for label, *neighbors in nodes:
            self.graph[label] = neighbors
        print(self.graph)


serialized_str = "0,1,2#1,2#2,2"
print(Graph(serialized_str))