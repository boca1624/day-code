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

    def size(self):
        return len(self.items)

def validate_stack_operations(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3, "Pop should return the last item added"
    assert stack.peek() == 2, "Peek should return the last item without removing it"
    assert stack.size() == 1, "Size should decrease after one item is popped"
    stack.push(4)
    assert stack.size() == 2, "Size should increase after pushing a new item"
    assert stack.is_empty() == False, "Stack should not be empty after adding items"
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True, "Stack should be empty after popping all items"
