class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [7,6,5,4,3,2,1]

        k = k % len(nums)
        def reversePortion(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reversePortion(0, len(nums) - 1)
        reversePortion(0, k - 1)
        reversePortion(k, len(nums) - 1)
        