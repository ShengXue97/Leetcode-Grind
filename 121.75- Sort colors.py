class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0, [0,0,2,1,1,2]
        # 2 -> put at current, 1 -> put at first 2, 0 -> put at first 1
        # [0,1,2,2,]
        # [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,0]
        # [0,1,1,1,1,2,2,2]
        # [1,1,1,1,0]
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1
            i += 1
        return nums