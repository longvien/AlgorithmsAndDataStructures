class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for k in range(m)]
        dp[0][0] = 1
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r == 0:
                    if dp[r][c] == 0:
                        dp[r][c] = dp[r][c-1]
                elif c == 0:
                    if dp[r][c] == 0:
                        dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]
mySolu = Solution()
print(mySolu.uniquePaths(3, 7))
