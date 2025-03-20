def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Sort the intervals in increasing order of start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track the end time of meetings
    import heapq
    heap = []

    # Add the first meeting. We have to give one room for the first meeting.
    heapq.heappush(heap, intervals[0][1])

    for i in intervals[1:]:
        # If the room due to free up the earliest is free, assign that room to this meeting
        if heap[0] <= i[0]:
            heapq.heappop(heap)

        # If a new room is to be assigned, then we add to the heap.
        heapq.heappush(heap, i[1])

    # The size of the heap tells us the minimum rooms required
    return len(heap)
