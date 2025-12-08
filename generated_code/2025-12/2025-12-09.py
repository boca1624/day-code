class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    # 如果当前节点为空或等于p或q，返回当前节点
    if not root or root == p or root == q:
        return root
