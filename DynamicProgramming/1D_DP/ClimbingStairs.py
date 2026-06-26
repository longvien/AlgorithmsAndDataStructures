#memoization
def climbingStairsM(n):
    dp = [-1 for i in range(n + 1)]
    return _climbingStairsM(n, dp)
def _climbingStairsM(n, dp):
    if n <= 2:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = _climbingStairsM(n - 1, dp) + _climbingStairsM(n - 2, dp)
    return dp[n]

print(climbingStairsM(7))

#tabulation
def climbingStairsT(n):
    dp = [-1 for i in range(n + 1)]
    if n <= 2:
        return n
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climbingStairsT(7))