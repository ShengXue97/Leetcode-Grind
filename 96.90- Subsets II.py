class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def recurse(cur_array, cur_index):
            res.append(cur_array[:])

            if cur_index >= len(nums):
                return
            
            prev = None
            for i in range(cur_index, len(nums)):
                if nums[i] == prev:
                    continue
                prev = nums[i]

                cur_array.append(nums[i])
                recurse(cur_array, i + 1)
                cur_array.pop()

        recurse([], 0)
        return res