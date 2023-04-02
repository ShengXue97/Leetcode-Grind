class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr_arr, curr_sum):
            if curr_sum == target:
                res.append(curr_arr.copy())
                return

            if i >= len(candidates) or curr_sum > target:
                return
        
            curr_arr.append(candidates[i])
            backtrack(i, curr_arr, curr_sum + candidates[i])
            curr_arr.pop()
            backtrack(i + 1, curr_arr, curr_sum)
        
        backtrack(0, [], 0)
        return res