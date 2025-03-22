# 二叉树的前序遍历和构建
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    
    root_index_in_inorder = inorder.index(root_val)
    
    root.left = buildTree(preorder[1:1+root_index_in_inorder], inorder[:root_index_in_inorder])
    root.right = buildTree(preorder[1+root_index_in_inorder:], inorder[root_index_in_inorder+1:])
    
    return root
