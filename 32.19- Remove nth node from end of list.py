# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        c = 0
        slow, fast = head, head
        while c < n:
            fast = fast.next
            c += 1
        
        # Out of list
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head