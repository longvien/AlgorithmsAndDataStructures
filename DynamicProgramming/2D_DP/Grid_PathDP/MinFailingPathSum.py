class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        dp = [[0 for i in range(m)] for i in range(n)]

        for i in range(m):
            dp[0][i] = matrix[0][i]
        for r in range(1, n):
            for c in range(m):
                if c == 0:
                    dp[r][c] = min(dp[r - 1][c+1], dp[r - 1][c]) + matrix[r][c]
                elif c == n-1:
                    dp[r][c] = min(dp[r - 1][c-1], dp[r - 1][c]) + matrix[r][c]
                else:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]) + matrix[r][c];
        return min(dp[n-1])
mySolu = Solution()
print(mySolu.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))