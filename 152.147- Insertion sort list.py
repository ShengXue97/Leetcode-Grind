# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedTail = head
        headCur = head.next
        sortedTail.next = None

        while headCur:
            nextt = headCur.next
            sortedCur = sortedTail
            prevSortedCur = None
            while sortedCur and sortedCur.val > headCur.val:
                prevSortedCur = sortedCur
                sortedCur = sortedCur.next

            if not prevSortedCur:
                headCur.next = sortedTail
                sortedTail = headCur
            else:
                prevSortedCur.next = headCur
                headCur.next = sortedCur
            headCur = nextt

        # Reverse result
        prev = None
        while sortedTail:
            nextt = sortedTail.next
            sortedTail.next = prev
            prev, sortedTail = sortedTail, nextt

        return prev
