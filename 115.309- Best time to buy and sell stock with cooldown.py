class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #Key: (index, buying), Value: Max profits

        def recurse(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Cooldown
            res = recurse(i + 1, buying)
            if buying:
                # Buy stock
                res = max(res, recurse(i + 1, False) - prices[i])
            else:
                # Sell stock, 2 because of cooldown
                res = max(res, recurse(i + 2, True) + prices[i])
            
            dp[(i, buying)] = res
            return res
        
        return recurse(0, True)