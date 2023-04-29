class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap = {}
        
        def dfs(i):
            if i not in preMap:
                preMap[i] = set()
                for neighbour in adjList[i]:
                    preMap[i] |= dfs(neighbour)
            
            preMap[i].add(i)
            return preMap[i]
    
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)

        for i in list(adjList.keys()):
            dfs(i)
        
        res = []
        for q1, q2 in queries:
            if q1 in preMap and q2 in preMap[q1]:
                res.append(True)
            else:
                res.append(False)
        return res