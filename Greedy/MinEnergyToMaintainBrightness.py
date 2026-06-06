import math
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=self.getKey)
        totalTime = 0
        bulbs = math.ceil(brightness / 3)
        start = 0
        current = 0
        i = 1
        if len(intervals) == 1: return (intervals[0][1] - intervals[0][0] + 1) * bulbs

        while i < len(intervals):
            if intervals[current][1] < intervals[i][0]:
                totalTime += intervals[current][1] - intervals[start][0] + 1
                start = i
                current = i
            elif intervals[current][1] >= intervals[i][0]:
                if intervals[current][1] <= intervals[i][1]:
                    current = i
            if i == len(intervals) - 1:
                totalTime += (intervals[current][1] - intervals[start][0] + 1)
                break
            i += 1

        return totalTime * bulbs

    def getKey(self, key):
        return key[0]