class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 2: 4, 3: 9, 4: 4
        scores = defaultdict(int)
        for num in nums:
            scores[num] += num
        
        keys = sorted(scores.keys())
        earn1, earn2 = 0, 0
        for i in range(len(keys)):
            if keys[i] - keys[i - 1] > 1:
                temp = earn2
                earn2 = scores[keys[i]] + earn2
                earn1 = temp
            else:
                temp = earn2
                earn2 = max(scores[keys[i]] + earn1, earn2)
                earn1 = temp
        
        return earn2