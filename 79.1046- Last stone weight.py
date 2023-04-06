class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_y = heapq.heappop(heap)
            stone_x = heapq.heappop(heap)
            if stone_y == stone_x:
                continue
            
            heapq.heappush(heap, stone_y - stone_x)
        
        if len(heap) == 0:
            return 0
        return -heap[0]