class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_balanced_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = build_balanced_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_balanced_tree(preorder[mid+1:], inorder[mid+1:])
    
    return root

def is_subtree(s, t):
    def dfs(node):
        if not node:
            return True
        if node.val == t.val and dfs(node.left) and dfs(node.right):
            return True
        return dfs(node.left) or dfs(node.right)
    
    stack = [s]
    while stack:
        node = stack.pop()
        if dfs(node):
            return True
        stack.extend([node.left, node.right])
    return False
