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
            for i in range(len(self.items) // 2):
                self.items[i], self.items[-1 - i] = self.items[-1 - i], self.items[i]

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.reverse()
print(q.dequeue())  # Output: 3
print(q.dequeue())  # Output: 2
print(q.dequeue())  # Output: 1
