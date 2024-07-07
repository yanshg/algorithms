'''
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:

Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1

Output: 200

Explanation:
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:

Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0

Output: 500

Explanation:
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

'''

# Dijstra

# hashmap to record cost and stops from the source to each city
# heapq to get cheapest price

from collections import defaultdict
import heapq

def get_cheapest_with_k_stops(n, edges, src, dest, k):
    # build graph
    graph = defaultdict(list)
    for s, d, p in edges:
        graph[s] += [ [ d, p ] ]

    # costs[city] = cost
    costs = [ float('inf') ] * n
    costs[src] = 0

    # heapq
    # cost, curr, stops
    hq = [[0, src, 0]]
    
    while hq:
        [ cost, curr, stops ] = heapq.heappop(hq)
        if stops > k or cost > costs[curr]:
            continue

        for next_dest, price in graph[curr]:
            next_cost = cost + price
            if next_cost < costs[next_dest]:
                costs[next_dest] = next_cost
                heapq.heappush(hq, [ next_cost, next_dest, stops + 1])

    return costs[dest] if costs[dest] != float('inf') else None

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(get_cheapest_with_k_stops(n, edges, src, dst, k))


