class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [1,2,3,4,5]
        # [3,4,5,1,2]
        # [-2,-2,-2,3,3]
        if sum(gas) < sum(cost):
            return -1

        best_station = 0
        cur_sum = -1

        for i in range(len(gas)):
            cur_station = gas[i] - cost[i]
            if cur_sum < 0:
                best_station = i
                cur_sum = cur_station
            else:
                cur_sum += cur_station
        
        return best_station