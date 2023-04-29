# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            nextt = cur.next
            cur.next = prev
            prev, cur = cur, nextt

        # leftPrev: Node before left, prev: Node at right, cur: Node after right
        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next