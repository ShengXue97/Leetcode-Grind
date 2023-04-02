class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [0, 0, 10, 15]
        n1, n2 = 0, 0
        for i in range(2, len(cost) + 1):
            temp = min(cost[i - 2] + n1, cost[i - 1] + n2)
            n1 = n2
            n2 = temp
        
        return n2