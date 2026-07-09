class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0 for i in range(n)] for i in range(n)]

        for i in range(1, n-1):
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1]

        for i in range(len(nums)-2, 0, -1):
            for j in range(i+1, len(nums)-1, 1):
                for k in range(i, j+1, 1):
                    left = 0
                    if k != i:
                        left = dp[i][k-1]
                    right = 0
                    if k != j:
                        right = dp[k+1][j]
                    dp[i][j] = max(dp[i][j], left + right + nums[i-1] * nums[k] * nums[j+1])
        return dp[1][len(nums) - 2]