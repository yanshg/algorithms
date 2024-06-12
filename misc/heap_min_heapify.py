def maxheap_to_minheap(maxheap):
    if not maxheap:
        return
    
    n = len(maxheap)
    if n == 1:
        return
    
    def min_heapify(heap, i, n):
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        smallest = i
        if left_child < n and heap[left_child] < heap[smallest]:
            smallest = left_child
        if right_child < n and heap[right_child] < heap[smallest]:
            smallest = right_child
        
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            min_heapify(heap, smallest, n)

    for i in range((n-2)//2, -1, -1):
        min_heapify(maxheap, i, n)

maxheap = [21, 15, 12, 10, 14, 8, 35, 4, 8, 13, 9, 7, 6, 1]
maxheap_to_minheap(maxheap)
print(maxheap)