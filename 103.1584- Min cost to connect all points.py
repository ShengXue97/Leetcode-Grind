class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        selected = set()
        minHeap = [(0,0)]

        while len(selected) != len(points):
            dist, minPoint = heapq.heappop(minHeap)
            if minPoint in selected:
                continue

            res += dist
            selected.add(minPoint)
            
            for i in range(len(points)):
                if i not in selected:
                    heapq.heappush(minHeap, 
                                    (abs(points[minPoint][0] - points[i][0]) +\
                                        abs(points[minPoint][1] - points[i][1]), i))
        
        return res