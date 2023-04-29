# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode()
        bigger = ListNode()
        cur = head

        smallerHead = smaller
        biggerHead = bigger

        while cur:
            if cur.val < x:
                smaller.next = cur
                smaller = cur
            else:
                bigger.next = cur
                bigger = cur
            cur = cur.next
        
        bigger.next = None
        smaller.next = biggerHead.next
        return smallerHead.next