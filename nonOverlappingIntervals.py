class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        removeInterval = 0
        lastEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                removeInterval += 1
            else:
                lastEnd = intervals[i][1]
        
        return removeInterval
