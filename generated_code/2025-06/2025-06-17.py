# 题目思路：找出一棵二叉树中所有从根到叶子路径，其路径和等于给定值 targetSum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, targetSum: int):
    result = []

    def dfs(node, current_path, current_sum):
        if not node:
            return
        current_path.append(node.val)
        current_sum += node.val
        if not node.left and not node.right and current_sum == targetSum:
            result.append(list(current_path))
        else:
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
        current_path.pop()  # 回溯

    dfs(root, [], 0)
    return result

# 示例构造
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1

root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(
