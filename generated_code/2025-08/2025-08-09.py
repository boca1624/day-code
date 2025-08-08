import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, -item)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def heapify(self, array):
        for item in array:
            self.push(item)
        return self

    def get_max_heap(self):
        return [-item for item in self.heap]
