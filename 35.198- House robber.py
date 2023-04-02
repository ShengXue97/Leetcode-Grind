class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,2,3,1]
        # [1,2,4,4]

        # [2,7,9,3,1]
        # [2,7,11,11,12]
        if len(nums) == 1:
            return nums[0]

        n1, n2 = nums[0], max(nums[0], nums[1])
        if len(nums) == 2:
            return n2
        
        for i in range(2, len(nums)):
            tmp = n2
            n2 = max(n1 + nums[i], n2)
            n1 = tmp
        
        return n2
        
        
