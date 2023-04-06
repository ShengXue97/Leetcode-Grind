class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0: 0000
        # 1: 0001
        # 2: 0010
        # 3: 0011
        # 4: 0100
        # 5: 0101
        # 6: 0110
        # 7: 0111
        # 8: 1000
        # 9: 1001
        res = 0
        for i in range(len(nums)):
            res ^= i + 1
            res ^= nums[i]
        
        return res