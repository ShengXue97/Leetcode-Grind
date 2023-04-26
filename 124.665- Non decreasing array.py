class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 5,6,7,5,10
        prev = nums[0]
        curMax = float('-inf')
        isModified = False
        for i in range(1, len(nums)):
            if nums[i] < prev:
                if isModified:
                    return False
                isModified = True
                if i == 1:
                    prev = nums[i]
                elif nums[i] >= curMax:
                    prev = nums[i]
                else:
                    prev = nums[i - 1]
            else:
                prev = nums[i]
            curMax = max(curMax, nums[i - 1])
        return True
                