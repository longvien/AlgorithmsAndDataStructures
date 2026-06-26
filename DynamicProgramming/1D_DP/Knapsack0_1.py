def Knapsack(weights, values, maxW):
    dp = [0 for i in range(maxW + 1)]
    for i in range(len(weights)):
        for n in range(maxW, weights[i - 1], -1):
            if weights[i] <= n:
                dp[n] = max(dp[n], dp[n - weights[i]] + values[i])
    return dp[maxW]
print(Knapsack([1, 2, 3], [6, 10, 12], 5))