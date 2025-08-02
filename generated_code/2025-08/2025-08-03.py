class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root

def find_lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = find_lowest_common_ancestor(root.left, p, q)
    right = find_lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right
