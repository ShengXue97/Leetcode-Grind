class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 2,3
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            total = (mid * (mid + 1)) / 2
            if total == n:
                return mid
            elif total < n:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return res