class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,2,3,3,4,6,7,8]
        nums = defaultdict(int)
        for n in hand:
            nums[n] += 1
        
        keys = list(nums.keys())
        heapq.heapify(keys)

        while keys:
            key = keys[0]
            for i in range(key, key + groupSize):
                if i not in nums:
                    return False
                
                nums[i] -= 1
                if nums[i] == 0:
                    if i != keys[0]:
                        return False
                    heapq.heappop(keys)
        
        return True
                