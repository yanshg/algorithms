'''
In a given array, rotate a part of the array for which the index is given

Input:

An array arr.
Start index start, end index end (both inclusive).
Number of rotations k.

'''

def get_rotated_array(arr, k, direction):
    # rotate array with k times

    l = len(arr)
    k %= l

    if direction == 'left':
        k = l - k
    return arr[-k:] + arr[:-k]

def rotate_subarray(arr, start, end, k, direction = 'right'):
    # validate input
    if not arr:
        return arr
    
    if start < 0 or end >= len(arr) or start > end:
        print("Error input")
        return arr
    
    rotated_array = get_rotated_array(arr[start:end+1], k, direction)
    return arr[:start] + rotated_array + arr[end+1:]

arr = [1, 2, 3, 4, 5, 6, 7]
start = 2
end = 5
k = 2
direction = "right"
print(rotate_subarray(arr, start, end, k))