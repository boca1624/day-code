class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMaxDepth(root):
    if not root:
        return 0
    left_depth = findMaxDepth(root.left)
    right_depth = findMaxDepth(root.right)
    return max(left_depth, right_depth) + 1

def isBalanced(root):
    if not root:
        return True

    def depth(node):
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1

    return depth(root) != -1

# 示例树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

# 查找最大深度
print(findMaxDepth(root))  # 输出树的最大深度

# 检查是否平衡
print(isBalanced(root))  # 输出是否为平衡树
