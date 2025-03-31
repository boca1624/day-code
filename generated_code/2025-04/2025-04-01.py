from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.window_sum -= self.queue.popleft()
        
        self.queue.append(val)
        self.window_sum += val
        return self.window_sum / len(self.queue)

# 示例使用
ma = MovingAverage(3)
print(ma.next(1))  # 输出: 1.0
print(ma.next(10)) # 输出: 5.5
print(ma.next(3))  # 输出: 4.67
print(ma.next(5))  # 输出: 6.0
