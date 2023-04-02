class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2, 1, 1, 2
        # 2, 2, 3, 
        def rob_1(sub):
            if len(sub) == 1:
                return sub[0]

            n1, n2 = sub[0], max(sub[0], sub[1])
            if len(sub) == 2:
                return n2
            
            for i in range(2, len(sub)):
                tmp = n2
                n2 = max(n1 + sub[i], n2)
                n1 = tmp
            
            return n2

        if len(nums) == 1:
                return nums[0]
        return max(rob_1(nums[1:]), rob_1(nums[:len(nums) - 1]))
        
