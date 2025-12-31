'''
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph. If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is_eventually safe _if and only if we must eventually walk to a terminal node. More specifically, there exists a natural numberKso that for any choice of where to walk, we must have stopped at a terminal node in less thanKsteps.

Which nodes are eventually safe? Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph. The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Copy
Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]

Output:
[2,4,5,6]
Here is a diagram of the above graph.

'''

from collections import defaultdict

class Graph:
    def __init__(self, maj_list):
        self.pre = defaultdict(set)
        self.suc = defaultdict(set)
        for i, neighs in enumerate(maj_list):
            for j in neighs:
                self.suc[i].add(j)
                self.pre[j].add(i)

        self.all_nodes = range(len(maj_list))

    def __repr__(self):
        return f"pre: {self.pre}, suc: {self.suc}"

    def get_safe_nodes(self):
        order = []

        todo = [ t for t in self.all_nodes if not self.suc[t] ]
        while todo:
            t = todo.pop()
            order.append(t)

            for p in self.pre[t]:
                self.suc[p].discard(t)
                if not self.suc[p]:
                    todo.append(p)
    
        return sorted(order)

maj_list = [[1,2],[2,3],[5],[0],[5],[],[]]
safe_nodes = [ 2, 4, 5, 6 ]
graph = Graph(maj_list)
print(graph)
assert graph.get_safe_nodes() == safe_nodes
