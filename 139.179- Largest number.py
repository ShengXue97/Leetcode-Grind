class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 903, 810, 9, 5, 4
        # 34, 3, 4, 346, 7
        # 9, 5, 34, 30, 3
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))