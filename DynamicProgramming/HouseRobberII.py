class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 4: return max(nums)
        dp = [0 for i in range(len(nums))]
        dp1 = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        dp[len(nums) - 1] = max(nums[len(nums) - 1], dp[len(nums) - 2])

        dp1[len(nums) - 1] = nums[len(nums) - 1]
        dp1[len(nums) - 2] = max(dp1[len(nums) - 1], nums[len(nums) - 2])
        for i in range(len(nums) - 3, 0, -1):
            dp1[i] = max(dp1[i + 1], dp1[i + 2] + nums[i])
        dp1[0] = max(nums[0], dp1[1])

        return max(max(dp), max(dp1))