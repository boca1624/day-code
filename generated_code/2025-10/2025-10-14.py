class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not inorder or not preorder:
        return None

    root_value = preorder[0]
    root = Node(root_value)
    root_index = inorder.index(root_value)

    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []
