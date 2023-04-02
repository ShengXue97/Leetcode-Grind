class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for i in range(1, len(dp)):
            smallest = float('inf')
            for c in coins:
                if i - c >= 0:
                    smallest = min(smallest, 1 + dp[i - c])
            dp[i] = smallest
        
        res = dp[amount]
        if res == float('inf'):
            return -1
        return res