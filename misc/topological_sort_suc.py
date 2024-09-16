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

class Graph:
    def __init__(self, maj_list):
        self.graph = maj_list

        pre = {}
        suc = {}
        for i in range(len(maj_list)):
            pre[i] = set()
            suc[i] = set()

        for i, neighs in enumerate(maj_list):
            for j in neighs:
                suc[i].add(j)
                pre[j].add(i)
        
        self.pre = pre
        self.suc = suc

    def __repr(self):
        return f"graph: {self.graph}, pre: {self.pre}, suc: {self.suc}"

def get_safe_nodes(graph):   
    order = []
    todo = set()
    for i in graph.suc:
        if not graph.suc[i]:
            todo.add(i)

    while todo:
        s = todo.pop()
        order.append(s)

        for p in graph.pre[s]:
            graph.suc[p].discard(s)
            if not graph.suc[p]:
                todo.add(p)
    
    return sorted(order)

maj_list = [[1,2],[2,3],[5],[0],[5],[],[]]
graph = Graph(maj_list)
print(graph)
print(get_safe_nodes(graph))