class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        # [2,2,4,3,3,2,1,1]

        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            largest = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    largest = max(largest, dp[j])
            dp[i] += largest
        return max(dp)