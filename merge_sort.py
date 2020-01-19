#!/usr/bin/python

def merge_sort(arr):
    l=len(arr)
    if l>1:
        mid=int(l/2)
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr,L,R)

def merge(arr,arr_left,arr_right):
    len_left=len(arr_left)
    len_right=len(arr_right)

    i=j=k=0
    while j<len_left and k<len_right:
        if arr_left[j] <= arr_right[k]:
            arr[i]=arr_left[j]
            j+=1
        else:
            arr[i]=arr_right[k]
            k+=1
        i+=1
    while j<len_left:
        arr[i]=arr_left[j]
        j+=1
        i+=1
    while k<len_right:
        arr[i]=arr_right[k]
        k+=1
        i+=1

if __name__ == '__main__':
    numbers=[ 21, 14, 6, 51, 23, 7, 25, 23, 22, 33, 6, 44, 23, 15, 51, 76 ]
    print("numbers: ", numbers)
    merge_sort(numbers)
    print("numbers after merge sort: ", numbers)

