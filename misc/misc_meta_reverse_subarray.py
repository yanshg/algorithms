'''
Given a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) reverse the order of the elements
'''

def reverse_subarray(arr, start, end):
    # validate input
    if not arr:
        return arr
    
    start -= 1
    end -= 1

    if start < 0 or end >= len(arr) or start > end:
        print("wrong input")
        return arr
    
    while start < end:
        # reverse arr[start] and arr[end]
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1

    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
start, end = 2, 5
result = reverse_subarray(arr, start, end)
print("Modified array:", result) 
