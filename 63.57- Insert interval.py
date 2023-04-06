class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        isInserted = False
        for interval in intervals:
            if interval[0] > newInterval[1]:
                if not isInserted:
                    isInserted = True
                    res.append(newInterval)
                res.append(interval)
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]),
                                max(interval[1], newInterval[1])]
        
        if not isInserted:
            res.append(newInterval)

        return res