'''
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

'''

def linear_search(arr):
    res = -1
    for i, num in enumerate(arr):
        if num == i:
            res = num
            break
    return res

def binary_search(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
        
    return False

arr = [-6, 0, 2, 40]
print(linear_search(arr))
print(binary_search(arr))

arr = [1, 5, 7, 8]
print(linear_search(arr))
print(binary_search(arr))
