class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert_key(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) <= 0:
            return float('-inf')
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def increase_key(self
