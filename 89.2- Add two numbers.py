# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # [9,9,9,9,9,9,9]
        # [9,9,9,9]
        # [8,9,9,9,]

        carryOver = 0
        res = ListNode()
        curNode = res
        while l1 or l2:
            l1v = 0
            l2v = 0
            if l1:
                l1v = l1.val
                l1 = l1.next
            if l2:
                l2v = l2.val
                l2 = l2.next
            
            curVal = l1v + l2v + carryOver
            if curVal >= 10:
                curVal -= 10
                carryOver = 1
            else:
                carryOver = 0
            
            newNode = ListNode(curVal)
            curNode.next = newNode
            curNode = curNode.next
            
        
        if carryOver:
            newNode = ListNode(carryOver)
            curNode.next = newNode
        
        return res.next



                

        

