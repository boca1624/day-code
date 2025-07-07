class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: TreeNode):
    if not root:
        return None
    
    # Helper function to flatten the tree in place
    def flatten_helper(node):
        if not node:
            return None
        
        if not node.left and not node.right:
            return node
        
        # Flatten left subtree
        left_tail = flatten_helper(node.left)
        
        # Flatten right subtree
        right_tail = flatten_helper(node.right)
        
        # If left subtree exists, we need to connect it with the right
        if node.left:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        # Return the last node in the flattened tree
        return right_tail if right_tail else left_tail
    
    flatten_helper(root)
