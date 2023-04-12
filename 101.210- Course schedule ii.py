class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        adjList = defaultdict(list)
        inDegrees = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            inDegrees[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbour in adjList[course]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(res) == numCourses:
            return res
        return []
        
    
