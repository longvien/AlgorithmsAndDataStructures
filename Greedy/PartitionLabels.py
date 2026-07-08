class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        intervals = []
        indexes = {}
        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = []
            indexes[s[i]].append(i)
        for k in indexes:
            intervals.append([min(indexes[k]), max(indexes[k])])
        intervals.sort(key=self.getKey)
        minI = intervals[0][0]
        maxI = intervals[0][1]
        i = 1
        while i < len(intervals):
            if intervals[i][0] > maxI:
                ans.append(maxI - minI + 1)
                minI = intervals[i][0]
                maxI = intervals[i][1]
            elif intervals[i][0] < maxI:
                if intervals[i][1] > maxI:
                    maxI = intervals[i][1]
            if i == len(intervals) - 1:
                ans.append(maxI - minI + 1)
                minI = intervals[i][0]
                maxI = intervals[i][1]
            i += 1
        return ans

    def getKey(self, key):
        return key[0]


