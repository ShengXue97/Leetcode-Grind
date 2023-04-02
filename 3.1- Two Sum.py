class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in s:
                return (s[n], i)
            s[target - n] = i
