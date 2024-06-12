'''

743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

'''

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:        
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        delays = [ float('inf') ] * (n + 1)
        delays[k] = 0
        
        hq = [ (0, k) ]
        max_delay = float('-inf')
        
        while hq:
            dist, v = heapq.heappop(hq)
            if delays[v] > dist:
                continue
                
            for u, w in graph[v]:
                new_dist = dist + w
                if new_dist < delays[u]:
                    delays[u] = new_dist
                    heapq.heappush(hq, (new_dist, u))
        
        for v in range(1,n+1):
            if delays[v] == float('inf'):
                return -1
            max_delay = max(max_delay, delays[v])
            
        return max_delay

solution = Solution()

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
solution.networkDelayTime(times, n, k) == 2


