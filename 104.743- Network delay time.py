class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        visited = set()
        minHeap = [(0, k)]
        
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            res = max(res, dist)
            for neighbour, weight in adjList[node]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (dist + weight, neighbour))
        
        if len(visited) == n:
            return res
        return -1
            
