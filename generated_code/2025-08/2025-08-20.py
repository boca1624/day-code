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

    def size(self):
        return len(self.items)

    def reverse(self):
        if not self.is_empty():
            self.items.reverse()

# 使用队列实现括号匹配验证
def is_valid(s: str) -> bool:
    queue = Queue()
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            queue.enqueue(char)
        elif char in mapping:
            if queue.is_empty() or queue.dequeue() != mapping[char]:
                return False
    return queue.is_empty()
