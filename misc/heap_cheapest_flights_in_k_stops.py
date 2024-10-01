'''
finding the cheapest price to travel from a source city to a destination city with at most ( k ) stops. This can be efficiently solved using the Bellman-Ford algorithm, which is well-suited for finding the shortest paths in a graph with weighted edges.
'''

def find_cheapest_price(n, flights, src, dst, k):
    # Initialize distances with infinity
    distances = [float('inf')] * n
    distances[src] = 0

    # Relax edges up to k+1 times
    for _ in range(k + 1):
        new_distances = distances[:]
        for u, v, price in flights:
            if distances[u] != float('inf') and distances[u] + price < new_distances[v]:
                new_distances[v] = distances[u] + price
        distances = new_distances

    return distances[dst] if distances[dst] != float('inf') else -1

# Example usage
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(find_cheapest_price(n, flights, src, dst, k))  # Output: 700
