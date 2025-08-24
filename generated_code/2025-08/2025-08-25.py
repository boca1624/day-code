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
        return self.items[::-1]

# 示例使用
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

reversed_queue = queue.reverse()
print(reversed_queue)  # 输出: [3, 2, 1]
