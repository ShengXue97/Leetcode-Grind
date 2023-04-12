class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) -1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1

            for j in range(1, amount + 1):
                nextDp[j] = dp[j]
                if j - coins[i] >= 0:
                    nextDp[j] += nextDp[j - coins[i]]
            dp = nextDp
        
        return dp[amount]
                