class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        maxSqr = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    if matrix[r][c] == '1':
                        dp[r][c] = 1
                        maxSqr = max(maxSqr, dp[r][c])
                    continue
                elif matrix[r][c] == '1':
                    dp[r][c] = 1
                    maxSqr = max(maxSqr, dp[r][c])
                if r != 0 and c != 0 and matrix[r][c] == '1' and matrix[r-1][c-1] == '1' and matrix[r-1][c] == '1' and matrix[r][c-1] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) + 1
                    maxSqr = max(maxSqr, dp[r][c])
        return maxSqr**2
    
mySolu = Solution()
print(mySolu.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))