from collections import deque

# 创建一个队列
queue = deque()

# 入队操作
queue.append(1)
queue.append(2)
queue.append(3)

# 出队操作
print(queue.popleft())  # 输出 1

# 查看队列的当前状态
print(queue)  # 输出 deque([2, 3])

# 查看队头元素
print(queue[0])  # 输出 2
