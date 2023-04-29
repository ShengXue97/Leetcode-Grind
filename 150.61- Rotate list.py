# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        count = head
        while count:
            size += 1
            count = count.next
        
        if not head:
            return head
        k = k % size
        if k == 0:
            return head
        
        cur = head
        for i in range(size - k - 1):
            cur = cur.next
        
        start = cur.next
        cur.next = None

        cur = start
        for i in range(k - 1):
            cur = cur.next
        cur.next = head
        return start
