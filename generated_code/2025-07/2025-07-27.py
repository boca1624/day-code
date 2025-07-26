class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_bst(n):
    if n <= 0:
        return None
    mid = n // 2
    root = Node(mid)
    root.left = generate_bst(mid)
    root.right = generate_bst(n - mid - 1)
    return root

def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.value)
        result += inorder_traversal(root.right)
    return result

def is_symmetric(root):
    if not root or (not root.left and not root.right):
        return True
    if root.left and root.right:
        return (root.left.value == root.right.value and
                is_symmetric(root.left.left) and
                is_symmetric(root.left.right) and
                is_symmetric(root.right.left) and
                is_symmetric(root.right.right))
    return False

# Example usage:
n = 5
bst = generate_bst(n)
print("Inorder Traversal:", inorder_traversal(bst))
print("Is Symmetric:", is_symmetric(bst))
