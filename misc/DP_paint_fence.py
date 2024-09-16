'''
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
'''


# https://www.geeksforgeeks.org/painting-fence-algorithm/


def paint_fence_ways(n, k):
    if n == 0 or k == 0:
        return 0
    
    if n == 1:
        return k
    
    if n == 2:
        return k * k
    
    return (paint_fence_ways(n-2, k) + paint_fence_ways(n-1, k)) * (k-1)