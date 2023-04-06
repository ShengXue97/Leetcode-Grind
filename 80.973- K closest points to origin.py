class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = (point[0] ** 2) + (point[1] ** 2)
            heap.append((dist, point))
        heapq.heapify(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res