'''
The “Cutting Ribbons” problem involves finding the maximum length of ribbon pieces you can obtain from a given set of ribbons such that you can get at least ( k ) pieces of the same length. 

This problem can be efficiently solved using a binary search approach.
'''

def max_length(ribbons, k):
    def can_cut(length):
        return sum(ribbon // length for ribbon in ribbons) >= k

    left, right = 1, max(ribbons)
    while left < right:
        mid = (left + right + 1) // 2
        if can_cut(mid):
            left = mid
        else:
            right = mid - 1

    return left

# Example usage
ribbons = [9, 7, 5]
k = 3
print(max_length(ribbons, k))  # Output: 5
