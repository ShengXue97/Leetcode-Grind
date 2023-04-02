class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort: 0,1,2,3,4,k
        c = Counter(nums)
        buckets = [[] for i in range(len(nums))]
        
        for key, value in c.items():
            buckets[value - 1].append(key)

        result = []
        for i in range(len(nums) - 1, -1, -1):
            if len(result) >= k:
                break
            result += buckets[i]

        return result