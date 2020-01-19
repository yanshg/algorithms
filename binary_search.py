#!/usr/bin/python

def binary_search(numbers, search_num):
    low=0
    high=len(numbers)-1
    while (low <= high):
        middle=int((low+high)/2)
        middle_num=numbers[middle]
        if search_num == middle_num:
           return middle
        elif search_num > middle_num:
           low=middle+1
        else:
           high=middle-1
    return -1

if __name__ == '__main__':
    numbers=[1,4,7,9,12,15,23,45,56,78]
    search=78
    result=binary_search(numbers,search)
    print("numbers: ", numbers)
    print("search: ", search)
    print("result: ", result)
