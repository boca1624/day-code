def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # 按照开始时间排序
    intervals.sort(key=lambda x: x[0])
    
    # 使用一个堆来跟踪正在进行的会议
    import heapq
    heap = []
    
    # 将第一个会议的结束时间加入堆中
    heapq.heappush(heap, intervals[0][1])
    
    for i in intervals[1:]:
        # 如果当前会议的开始时间大于等于堆顶的结束时间，则可以复用会议室
        if i[0] >= heap[0]:
            heapq.heappop(heap)
        
        # 将当前会议的结束时间加入堆中
        heapq.heappush(heap, i[1])
    
    # 堆的大小即为需要的会议室数
    return len(heap)
