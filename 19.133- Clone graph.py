"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def traverse(root):
            if root:
                if root.val in visited:
                    return
                
                newNeighbours = []
                newNode = Node(root.val, newNeighbours)
                visited[root.val] = newNode
                
                for n in root.neighbors:
                    traverse(n)
                    newNeighbours.append(visited[n.val])
            
                return newNode
        
        return traverse(node)