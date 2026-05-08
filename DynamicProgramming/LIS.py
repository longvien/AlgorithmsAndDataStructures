#LIS | Largest Increasing Subsequence
def LIS(nums) -> int:
    dp = [1 for i in range(len(nums) + 1)]
    if len(nums) == 1:
        return 1
    return _LIS(nums, dp, len(nums) - 1)
def _LIS(nums, dp, n):
    if n == 0:
        return 1
    if dp[n] != 1:
        return dp[n]
