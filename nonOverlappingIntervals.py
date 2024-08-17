class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        removeInterval = 0
        upperLimit = intervals[0][1]
        lowerLimit = intervals[0][0]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < upperLimit:
                removeInterval += 1
            else:
                upperLimit = intervals[i][1]
                lowerLimit = intervals[i][0]
        
        return removeInterval
