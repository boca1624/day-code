# 二叉树：找出树中所有从根到叶子节点的路径，路径以字符串列表形式返回
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        result = []

        def dfs(node: TreeNode, path: List[str]):
            if not node.left and not node.right:
                result.append("->".join(path + [str(node.val)]))
                return
            if node.left:
                dfs(node.left, path + [str(node.val)])
            if node.right:
                dfs(node.right, path + [str(node.val)])

        dfs(root, [])
        return result

# 示例构建和调用
#      1
#     / \
#    2   3
#     \
#      5
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
sol = Solution()
print(sol.binaryTreePaths(root))  # 输出: ["1->2->5", "1->3"]
