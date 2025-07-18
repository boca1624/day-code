import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

# 示例
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # 返回 4
print(kthLargest.add(5))  # 返回 5
print(kthLargest.add(10)) # 返回 5
print(kthLargest.add(9))  # 返回 8
print(kthLargest.add(4))  # 返回 8
