class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        l = len(costs)
        a = l // 2
        b = l // 2
        n = l - 1
        total = 0
        limit = False
        costs.sort(key=self.sortDifference)
        while n >= 0:
            if costs[n][0] > costs[n][1]:
                total += costs[n][1]
                b -= 1
            else:
                total += costs[n][0]
                a -= 1
            n -= 1
            if a == 0 or b == 0:
                limit = True
                break
        if limit:
            if a > b:
                for i in range(n, -1, -1):
                    total += costs[i][0]
            else:
                for i in range(n, -1, -1):
                    total += costs[i][1]
        return total
    def sortDifference(self, pair):
        return abs(pair[0] - pair[1])

#leetcode, task 1029