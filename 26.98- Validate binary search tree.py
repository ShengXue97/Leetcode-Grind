# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, minv, maxv):
            if not node:
                return True
            if node.val <= minv or node.val >= maxv:
                return False
            return traverse(node.left, minv, min(maxv, node.val)) and\
                    traverse(node.right, max(minv, node.val),maxv)
        
        return traverse(root, float('-inf'), float('inf'))
        
