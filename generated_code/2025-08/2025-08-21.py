import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

# Example usage:
max_heap = MaxHeap()
max_heap.push(3)
max_heap.push(1)
max_heap.push(4)

print(max_heap.pop())  # Output: 4
print(max_heap.peek()) # Output: 3
print(max_heap.is_empty()) # Output: False
print(max_heap.size()) # Output: 2
