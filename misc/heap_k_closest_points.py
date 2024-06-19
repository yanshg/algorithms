'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq

def get_k_closest_points_to_origin(points, k):
    hq = []

    i = 0
    for x, y in points:
        dist = - (x * x + y * y)
        if i < k:
            heapq.heappush(hq, (dist, x, y))
        elif dist > hq[0][0]:
            heapq.heappushpop(hq, (dist, x, y))
        i += 1

    return [ (x, y) for dist, x, y in hq ]
    
points = [[1,3],[-2,2]] 
k = 1
print(get_k_closest_points_to_origin(points, k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(get_k_closest_points_to_origin(points, k))
