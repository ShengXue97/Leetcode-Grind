class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [3,3/6,-2/-12,]
        # -2,0,-1/0
        res, smallest, biggest = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp = min(smallest * n, biggest * n, n)
            biggest = max(smallest * n, biggest * n, n)
            smallest = temp

            res = max(res, biggest)
        
        return res

            