class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points: return 0
        if len(points) == 1: return 1
        total = 1
        points.sort(key=self.getKey)
        l = len(points)
        current = 0
        i = 1
        while i < l:
            if points[current][1] >= points[i][0] and points[current][1] <= points[i][1]:
                if i == l - 1:
                    break
                i += 1
            else:
                current = i
                total += 1
                if current == l - 1:
                    break
                i += 1
        return total

    def getKey(self, point):
        return point[1]