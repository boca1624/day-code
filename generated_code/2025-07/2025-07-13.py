class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果 min_stack 为空或当前值更小或相等，压入 min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Min stack is empty")


# 示例操作
s = MinStack()
s.push(5)
s.push(3)
s.push(7)
s.pop()
print("Top:", s.top())       # 输出 3
print("Min:", s.getMin())    # 输出 3
