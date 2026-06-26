class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        for c in range(1, len(grid[0])):
            dp[0][c] = dp[0][c - 1] + grid[0][c]
        for r in range(1, len(grid)):
            dp[r][0] = dp[r - 1][0] + grid[r][0]
        for rows in range(1, len(grid)):
            for cols in range(1, len(grid[0])):
                dp[rows][cols] = min(dp[rows - 1][cols], dp[rows][cols - 1]) + grid[rows][cols]
        return dp[len(grid) - 1][len(grid[0]) - 1]
mySolu = Solution()
print(mySolu.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))