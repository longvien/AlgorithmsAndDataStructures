class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        rN = len(obstacleGrid)
        cN = len(obstacleGrid[0])
        dp = [[0 for i in range(cN)] for n in range(rN)]
        dp[0][0] = 1
        for i in range(1, cN):
            if i < cN:
                if obstacleGrid[0][i] == 1:
                    break
                dp[0][i] = 1
        for j in range(1, rN):
            if j < rN:
                if obstacleGrid[j][0] == 1:
                    break
                dp[j][0] = 1
        for r in range(1, rN):
            for c in range(1, cN):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[rN-1][cN-1]