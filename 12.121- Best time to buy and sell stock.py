class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]

        for n in prices:
            res = max(res, n - min_price)
            min_price = min(min_price, n)
            
        return res