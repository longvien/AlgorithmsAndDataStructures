class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0
        if amount == 0:
            return 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]