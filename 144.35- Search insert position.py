class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Find first index that is >= target
        nums.append(target)
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return r
        