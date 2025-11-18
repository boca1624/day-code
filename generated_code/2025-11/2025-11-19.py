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

def validate_brackets(expression):
    stack = Stack()
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False
    return stack.is_empty()
