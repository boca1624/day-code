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

# 实例化队列
queue = Queue()

# 模拟队列操作
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# 队列的遍历
while not queue.is_empty():
    print(queue.dequeue())
