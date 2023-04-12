class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def search(num):
            p = parent[num]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        # Return false if already unioned
        def union(num1, num2):
            p1 = search(num1)
            p2 = search(num2)
            if p1 == p2:
                return False

            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge