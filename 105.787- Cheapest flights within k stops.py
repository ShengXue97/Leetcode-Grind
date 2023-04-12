class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for i in range(n)]
        prices[src] = 0

        for i in range(k + 1):
            temp = prices[:]
            for s, d, p in flights:
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            prices = temp
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]