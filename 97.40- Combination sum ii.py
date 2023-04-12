class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def recurse(i, curArr, curSum):
            if curSum == target:
                res.append(curArr[:])
                return

            if i >= len(candidates) or curSum > target:
                return

            curArr.append(candidates[i])
            recurse(i + 1, curArr, curSum + candidates[i])
            curArr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            recurse(i + 1, curArr, curSum)
        
        recurse(0, [], 0)
        return res
            
