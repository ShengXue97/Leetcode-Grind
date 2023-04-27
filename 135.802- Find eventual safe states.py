class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeMap = {}

        def dfs(i):
            if i in safeMap:
                return safeMap[i]

            safeMap[i] = False
            for j in graph[i]:
                if not dfs(j):
                    return False
            
            safeMap[i] = True
            return True
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res