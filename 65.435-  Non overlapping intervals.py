class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2],[1,3],[2,3],[3,4]]
        intervals.sort(key = lambda x:x[0])
        res = 0
        curEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < curEnd:
                # Remove the interval with the later end
                res += 1
                curEnd = min(curEnd, interval[1])
            else:
                curEnd = interval[1]
        
        return res
