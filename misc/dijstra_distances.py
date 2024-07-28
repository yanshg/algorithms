#!/usr/bin/python

import heapq

def dijstra_distances(graph, start):
    distances = { vertice:float('inf') for vertice in graph }
    distances[start] = 0

    hq = [(0, start)]
    while hq:
        current_distance, current_vertice = heapq.heappop(hq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertice the first time we remove it from the priority queue.
        if current_distance > distances[current_vertice]:
            continue

        for neighbor,weight in graph[current_vertice].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(hq, (distance, neighbor))

    return distances

graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(dijstra_distances(graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
