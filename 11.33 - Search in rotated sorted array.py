class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l < r):
            print(l, r)
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if target < nums[m]:
                if nums[m] < nums[l] or nums[l] < nums[r]:
                    r = m - 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > nums[l]:
                    l = m + 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        if nums[l] == target:
            return l
        return -1