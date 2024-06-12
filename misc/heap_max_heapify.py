def minheap_to_maxheap(min_heap):
    if not min_heap:
        return
    
    n = len(min_heap)
    if n == 1:
        return
    
    def max_heapify(heap, i, n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        largest = i
        if left_child < n and heap[largest] < heap[left_child]:
            largest = left_child
        if right_child < n and heap[largest] < heap[right_child]:
            largest = right_child
        
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            max_heapify(heap, largest, n)

    for i in range((n-2)//2, -1, -1):
        max_heapify(min_heap, i, n)


heap = [ 1, 4, 5, 8, 9, 6, 12, 10, 15, 13, 14, 7, 8, 21]
minheap_to_maxheap(heap)
print(heap)