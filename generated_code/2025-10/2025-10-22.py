class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def get_min(self):
        min_stack = []
        for item in self.items:
            if not min_stack or item > min_stack[-1]:
                min_stack.append(item)
            else:
                min_stack.append(min_stack[-1])
        return min_stack[-1]

stack = Stack()
stack.push(3)
stack.push(1)
stack.push(2)
print(stack.get_min())  # Output should be 1
stack.pop()
print(stack.get_min())  # Output should be 1
