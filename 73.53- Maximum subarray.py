class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0
        for num in nums:
            if cur > 0:
                cur += num
            else:
                cur = num
            res = max(res, cur)
        
        return res