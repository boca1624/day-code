class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    if not root:
        return None
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root

def sum_of_left_leaves(root):
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sum_of_left_leaves(root.right)
    return sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)
