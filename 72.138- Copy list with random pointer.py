"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        first = head
        oldToNew = {}
        while head:
            newNode = Node(head.val)
            oldToNew[head] = newNode
            head = head.next
        
        for k, v in oldToNew.items():
            if k.next:
                v.next = oldToNew[k.next]
            if k.random:
                v.random = oldToNew[k.random]
        
        return oldToNew[first]