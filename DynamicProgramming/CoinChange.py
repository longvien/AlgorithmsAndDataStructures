def coinChange(cost, amount):
    dp = [float("inf") for i in range(amount + 1)]
    dp[0] = 0
    result =  _coinChange(cost, amount, dp)
    if result == float("inf"):
        return -1
    return result
def _coinChange(cost, amount, dp):
    if amount == 0:
        return 0
    if dp[amount] != float("inf"):
        return dp[amount]
    for c in cost:
        if c <= amount:
            dp[amount] = min(dp[amount], _coinChange(cost, amount - c, dp) + 1)
    return dp[amount]

cost = [186,419,83,408]
print(coinChange(cost, 6249))

