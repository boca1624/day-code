from collections import deque

class MyQueue:
    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else None

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1] if self.out_stack else None

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
