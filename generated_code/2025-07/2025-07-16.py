import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 最大堆（Python中用负数实现最大堆）
        self.min_heap = []  # 最小堆

    def addNum(self, num: int) -> None:
        # 保持两个堆的平衡
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)  # 负数模拟最大堆
        else:
            heapq.heappush(self.min_heap, num)

        # 调整堆的大小差距，保证最大堆和最小堆的元素数量差不超过1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
