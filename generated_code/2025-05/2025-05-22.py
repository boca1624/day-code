from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        
        self.queue.append(val)
        self.total += val
        
        return self.total / len(self.queue)

# 示例用法
m_avg = MovingAverage(3)
print(m_avg.next(1))  # 返回 1.0
print(m_avg.next(10)) # 返回 5.5
print(m_avg.next(3))  # 返回 4.66667
print(m_avg.next(5))  # 返回 6.0
