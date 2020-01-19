#!/usr/bin/python

# Ways to choose pivot
#    1. The first element
#    2. The last element
#    3. The medium element
#
# Get position which (the number at the position NEED NOT be the pivot):
#     the left part <= pivot
#     the right part >= pivot
#

def quick_sort(numbers,left,right):
    if left<right:
        index=partition(numbers,left,right)
        quick_sort(numbers,left,index-1)
        quick_sort(numbers,index,right)

# must use 'numbers[left]<pivot' and 'numbers[right]>pivot',
# otherwise, loop infinite.

def partition(numbers,left,right):
    pivot=numbers[(left+right)//2]
    while left<=right:
        while numbers[left]<pivot:
            left+=1
        while numbers[right]>pivot:
            right-=1
        if left<=right:
            numbers[left],numbers[right]=numbers[right],numbers[left]
            left+=1
            right-=1
    return left;

if __name__ == '__main__':
    numbers=[ 21, 14, 6, 51, 23, 7, 25, 23, 22, 33, 6, 44, 23, 15, 51, 76 ]
    length=len(numbers)
    print("numbers: ", numbers)
    quick_sort(numbers, 0, length-1)
    print("numbers after quick sort: ", numbers)

