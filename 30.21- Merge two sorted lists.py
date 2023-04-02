# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode()
        resTail = resHead

        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                resTail.next = list1
                resTail = resTail.next
                list1 = list1.next
            else:
                resTail.next = list2
                resTail = resTail.next
                list2 = list2.next
            
        
        return resHead.next