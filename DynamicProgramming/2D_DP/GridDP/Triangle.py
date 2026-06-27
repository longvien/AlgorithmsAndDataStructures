class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nr = len(triangle)
        dp = [[0 for n in range(i + 1)] for i in range(nr)]
        dp[0][0] = triangle[0][0]
        for r in range(1, nr):
            for c in range(r+1):
                if c == 0:
                    dp[r][c] = dp[r-1][c] + triangle[r][c]
                elif c == r:
                    dp[r][c] = dp[r-1][c-1] + triangle[r][c]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c-1]) + triangle[r][c]
        return min(dp[nr-1])

