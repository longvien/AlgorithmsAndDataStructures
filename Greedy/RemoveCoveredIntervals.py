class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        i = 1
        intervals.sort(key=self.sortStart)
        start = intervals[0][0]
        end = intervals[0][1]

        while i < len(intervals):
            if start <= intervals[i][0] and intervals[i][1] <= end:
                count += 1
            elif intervals[i][0] <= start and end <= intervals[i][1]:
                count += 1
                start = intervals[i][0]
                end = intervals[i][1]
            else :
                start = intervals[i][0]
                end = intervals[i][1]
            i += 1
        return len(intervals) - count
    def sortStart(self, key):
        return key[0]