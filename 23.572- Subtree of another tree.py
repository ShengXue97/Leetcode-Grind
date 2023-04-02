# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                return isSameTree(node1.left, node2.left) and\
                        isSameTree(node1.right, node2.right)
            else:
                return False
        
        if not subRoot:
            return True
        if not root:
            return False
        
        return isSameTree(root, subRoot) or\
                    self.isSubtree(root.left, subRoot) or\
                    self.isSubtree(root.right, subRoot)