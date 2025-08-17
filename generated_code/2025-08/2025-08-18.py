from collections import deque

def reverse_queue(q):
    if not q:
        return q
    
    # Reverse the queue using a stack (or recursion)
    stack = []
    while q:
        stack.append(q.popleft())
    
    # Reconstruct the queue from the stack
    while stack:
        q.append(stack.pop())
    
    return q

# Example usage
queue = deque([1, 2, 3, 4, 5])
reversed_queue = reverse_queue(queue)
print(reversed_queue)  # Output: deque([5, 4, 3, 2, 1])
