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
            left, right = 0, len(self.items) - 1
            while left < right:
                self.items[left], self.items[right] = self.items[right], self.items[left]
                left += 1
                right -= 1
