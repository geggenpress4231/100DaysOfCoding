import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize a min-heap to track the end times of meetings
    heap = []


    heapq.heappush(heap, intervals[0][1])

    for i in range(1, len(intervals)):
 
        if intervals[i][0] >= heap[0]:
            # Remove the earliest end time
            heapq.heappop(heap)

        heapq.heappush(heap, intervals[i][1])


    return len(heap)

