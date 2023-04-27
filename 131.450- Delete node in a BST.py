# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        dummy = TreeNode(left=root)
        prev = dummy
        cur = dummy.left
        isLeft = True
        isFound = False
        left, right = None, None

        while cur:
            if key < cur.val:
                prev = cur
                cur = cur.left
                isLeft = True
            elif key > cur.val:
                prev = cur
                cur = cur.right
                isLeft = False
            else:
                left = cur.left
                right = cur.right

                if isLeft:
                    prev.left = right
                else:
                    prev.right = right
                isFound = True
                break
        
        if not isFound:
            return dummy.left
        if not right:
            if isLeft:
                prev.left = left
            else:
                prev.right = left
            return dummy.left
        if not right.left:
            right.left = left
            return dummy.left
        if not left:
            return dummy.left
        # Insert left into BST, starting from prev
        prev = right
        cur = right.left
        
        isLeft = True
        while cur:
            if left.val < cur.val:
                prev = cur
                cur = cur.left
                isLeft = True
            elif key > cur.val:
                prev = cur
                cur = cur.right
                isLeft = False
        
        if isLeft:
            prev.left = left
        else:
            prev.right = left
        return dummy.left
