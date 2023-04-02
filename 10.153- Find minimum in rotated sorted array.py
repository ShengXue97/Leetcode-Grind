class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = (l + r) // 2
            if m > 0 and nums[m - 1] > nums[m]:
                return nums[m]
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return nums[l]