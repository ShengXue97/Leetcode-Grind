class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums) - 1:
            cur_max = l
            for i in range(l, r + 1):
                cur_max = max(cur_max, nums[i] + i)
            l = r + 1
            r = cur_max
            res += 1
        return res