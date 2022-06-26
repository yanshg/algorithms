def flatten_array(arr):
    if isinstance(arr, list):
        for item in arr:
            yield from flatten_array(item)
    else:
        yield arr


arr = [ 1, 2, [3, 4], None, [], 5, [ 6, [7, 8], 9], 10]

new_arr = list(flatten_array(arr))

print(new_arr)
