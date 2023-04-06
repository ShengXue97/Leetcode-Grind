class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for num in nums:
            out ^= num
        return out