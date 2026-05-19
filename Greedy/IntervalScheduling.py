def IntervalScheduling(intervals):
    if not intervals:
        return intervals
    intervals.sort(key=getEnd)
    count = 1
    current = intervals[0]
    k = len(intervals)
    i = 1
    while i < k:
        if intervals[i][0] < current[1]:
            i += 1
            continue
        else:
            current = intervals[i]
            count += 1
            i += 1
    return count
def getEnd(interval):
    return interval[1]
print(IntervalScheduling([(1,100), (2,3), (3,4), (4,5)]))