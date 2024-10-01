'''
A “Valid Mountain Array” is an array that meets the following criteria:

Its length is at least 3.
There exists an index ( i ) such that:
The elements before ( i ) are in strictly increasing order.
The elements after ( i ) are in strictly decreasing order.
'''

def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0

    # Walk up
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Peak can't be first or last
    if i == 0 or i == n - 1:
        return False

    # Walk down
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

# Example usage
arr = [0, 3, 2, 1]
print(valid_mountain_array(arr))  # Output: True
