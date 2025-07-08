class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Only push to min_stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # Pop from min_stack only if it's the current minimum
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# 示例用法
s = MinStack()
s.push(5)
s.push(3)
s.push(7)
s.push(3)
s.pop()
print(s.getMin())  # 输出 3
s.pop()
print(s.getMin())  # 输出 3
s.pop()
print(s.getMin())  # 输出 5
