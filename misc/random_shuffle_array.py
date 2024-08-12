import random

num = 30

arr = list(range(num))

random.shuffle(arr)
print(arr)

for i in range(num):
    print(i)
    new_idx = arr[i]
    if i != new_idx:
        arr[i],arr[new_idx] = arr[new_idx],arr[i]
    print(arr)

