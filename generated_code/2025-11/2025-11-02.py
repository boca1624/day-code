class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def find_largest_bst_subtree(root):
    def largest_bst(node):
        if not node:
            return [True, float('-inf'), float('inf'), 1]
        
        is_bst = True
        left_min = node.value
        right_max = node.value
        left_size = 0
        right_size = 0
        
        left = largest_bst(node.left)
        right = largest_bst(node.right)
        
        if left[0] and right[0] and node.value > left[2] and node.value < right[1]:
            is_bst = True
            left_min = min(left_min, left[1])
            right_max = max(right_max, right[3])
            left_size = left[3]
            right_size = right[3]
        else:
            is_bst = False
        
        return [is_bst, left_min, right_max, left_size + right_size + 1]
    
    largest = 0
    def dfs(node):
        nonlocal largest
        if largest_bst(node)[0]:
            largest = max(largest, largest_bst(node)[3])
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
    
    dfs(root)
