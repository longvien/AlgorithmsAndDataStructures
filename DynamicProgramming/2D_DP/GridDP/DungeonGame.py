class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0 for i in range(m)] for i in range(n)]
        ans = 0 - dungeon[n-1][m-1] + 1
        if ans < 1:
            dp[n-1][m-1] = 1
        else:
            dp[n-1][m-1] = ans

        for i in range(n-2, -1, -1):
            ans = dp[i+1][m-1] - dungeon[i][m-1]
            if ans < 1:
                dp[i][m-1] = 1
            else:
                dp[i][m-1] = ans

        for i in range(m-2, -1, -1):
            ans = dp[n-1][i+1] - dungeon[n-1][i]
            if ans < 1:
                dp[n-1][i] = 1
            else:
                dp[n-1][i] = ans

        for r in range(n-2, -1, -1):
            for c in range(m-2, -1, -1):
                ans = min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c]
                if ans < 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = ans
        return dp[0][0]
