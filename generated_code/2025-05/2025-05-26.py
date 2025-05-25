def minMeetingRooms(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    end_times = []
    
    for interval in intervals:
        if end_times and end_times[0] <= interval[0]:
            heapq.heappop(end_times)
        heapq.heappush(end_times, interval[1])
    
    return len(end_times)

import heapq

# 示例调用
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))
