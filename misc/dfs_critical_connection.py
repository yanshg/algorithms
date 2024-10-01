def criticalConnections(n, connections):
    from collections import defaultdict

    def dfs(node, parent, discovery_time, low_time, time, graph, result):
        discovery_time[node] = low_time[node] = time
        time += 1

        for neighbor in graph[node]:
            if discovery_time[neighbor] == -1:  # If neighbor is not visited
                dfs(neighbor, node, discovery_time, low_time, time, graph, result)
                low_time[node] = min(low_time[node], low_time[neighbor])

                if low_time[neighbor] > discovery_time[node]:
                    result.append([node, neighbor])
            elif neighbor != parent:  # Update low_time if neighbor is not parent
                low_time[node] = min(low_time[node], discovery_time[neighbor])

    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    discovery_time = [-1] * n
    low_time = [-1] * n
    result = []

    for i in range(n):
        if discovery_time[i] == -1:
            dfs(i, -1, discovery_time, low_time, 0, graph, result)

    return result

# Example usage:
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(criticalConnections(n, connections))  # Output: [[1, 3]]
