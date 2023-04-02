class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(cur_array, cur_index):
            res.append(cur_array[:])

            if cur_index >= len(nums):
                return
            
            for i in range(cur_index, len(nums)):
                cur_array.append(nums[i])
                recurse(cur_array, i + 1)
                cur_array.pop()

        recurse([], 0)
        return res