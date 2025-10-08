class Solution:
    def find_min_cost_to_heap(self, nums):
        # 初始化最小堆
        import heapq
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
        
        # 贪心思想：每次取堆顶元素，然后与下一个元素合并，再放回堆中
        while len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            merged = first + second
            heapq.heappush(min_heap, merged)
        
        # 返回堆中剩余元素的总和，即最小成本
        return sum(min_heap)
