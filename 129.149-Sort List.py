# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(node):
            slow, fast, prev = node, node, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if not prev:
                return node
            
            prev.next = None
            left = mergeSort(node)
            right = mergeSort(slow)
            res = ListNode()
            resHead = res

            while left or right:
                if not left:
                    res.next = right
                    break
                elif not right:
                    res.next = left
                    break
                elif left.val < right.val:
                    res.next = left
                    left = left.next
                    res = res.next
                else:
                    res.next = right
                    right = right.next
                    res = res.next
            return resHead.next
        
        return mergeSort(head)
                