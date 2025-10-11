class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def reverse(self):
        if not self.is_empty():
            start = 0
            end = len(self.items) - 1
            while start < end:
                self.items[start], self.items[end] = self.items[end], self.items[start]
                start += 1
                end -= 1
        return self.items

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.reverse())  # Output: [3, 2, 1]
