'''
determining the minimum number of conference rooms needed to accommodate all given meeting time intervals
'''

import heapq

def minMeetingRooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize a min-heap to keep track of end times of meetings
    heap = []
    
    # Add the end time of the first meeting
    heapq.heappush(heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        # If the room due to free up the earliest is free, remove it from the heap
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        
        # Add the current meeting's end time to the heap
        heapq.heappush(heap, intervals[i][1])
    
    # The size of the heap is the number of rooms required
    return len(heap)

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2
