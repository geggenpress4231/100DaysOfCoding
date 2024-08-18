def canAttendMeetings(intervals):
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x[0])
    upperLimit = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < upperLimit:
            return False
        upperLimit = intervals[i][1]
    
    return True
