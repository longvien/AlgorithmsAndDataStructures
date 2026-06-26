#memoization
def coinChangeM(cost, amount):
    dp = [float("inf") for i in range(amount + 1)]
    dp[0] = 0
    result =  _coinChangeM(cost, amount, dp)
    if result == float("inf"):
        return -1
    return result
def _coinChangeM(cost, amount, dp):
    if amount == 0:
        return 0
    if dp[amount] != float("inf"):
        return dp[amount]
    for c in cost:
        if c <= amount:
            dp[amount] = min(dp[amount], _coinChangeM(cost, amount - c, dp) + 1)
    return dp[amount]

costM = [1, 3, 5]
print(coinChangeM(costM, 11))

#tabulation
def coinChangeT(cost, amount):
    dp = [float("inf") for i in range(amount + 1)]
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in cost:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]

costT = [2]
print(coinChangeT(costT, 3))