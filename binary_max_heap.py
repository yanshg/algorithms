#!/usr/bin/python

# Article: https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%8F%89%E5%A0%86%E8%AF%A6%E8%A7%A3%E5%AE%9E%E7%8E%B0%E4%BC%98%E5%85%88%E7%BA%A7%E9%98%9F%E5%88%97.md

# Implement binary max heap

class MaxHeap:
    def __init__(self, arr=[]):
        self.array=list()
        self.heapify(arr)

    def __len__(self):
        return len(self.array)

    def parent(self, k):
        return (k-1) // 2

    def left_child(self, k):
        return 2 * k + 1

    def right_child(self, k):
        return 2 * k + 2

    def heapify(self, arr):
        self.array = list()
        for v in arr:
            self.heappush(v)

    # Append and swim
    def heappush(self, v):
        self.array.append(v)
        self.swim(len(self.array) - 1)

    # Swap the last item with the first, and then sink
    def heappop(self):
        self.swap(0, len(self.array) - 1)
        self.sink(0)
        return self.array.pop()

    def get_max(self):
        l = len(self.array)
        return self.array[0] if l>0 else None

    def swap(self, i, j):
        l = len(self.array)
        assert i < l and j < l

        self.array[i],self.array[j]=self.array[j],self.array[i]

    def less(self, i, j):
        return self.array[i] < self.array[j]

    # Up
    def swim(self, k):
        p = self.parent(k)
        while k > 0 and self.array[p] < self.array[k]:
            self.swap(p, k)
            k = p
            p = self.parent(k)

    # Down
    def sink(self, k):
        l = len(self.array)
        assert k < l

        left_c, right_c = self.left_child(k), self.right_child(k)
        while left_c < l:
            bigger = left_c
            if right_c < l and self.less(left_c, right_c):
                bigger = right_c

            if self.less(bigger, k):
                break

            self.swap(k, bigger)
            k = bigger
            left_c, right_c = self.left_child(k), self.right_child(k)


mh=MaxHeap([3,2,6,5,4,1])
assert mh.heappop() == 6

mh.heappush(9)
assert mh.get_max() == 9
