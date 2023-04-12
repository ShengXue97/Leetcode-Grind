class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total / 2
        nums.sort()
        sums = set()
        sums.add(0)
        sums.add(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            if target in sums:
                return True
            
            temp = sums.copy()
            for n in temp:
                sums.add(n + nums[i])
        
        return target in sums
