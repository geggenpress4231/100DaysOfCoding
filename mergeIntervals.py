class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # Sort intervals by their start time
        mergedInterval = []
        i = 0

        while i < len(intervals):
            if mergedInterval and mergedInterval[-1][1] >= intervals[i][0]:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], intervals[i][1])
            else:
                mergedInterval.append(intervals[i])
            i += 1

        return mergedInterval
