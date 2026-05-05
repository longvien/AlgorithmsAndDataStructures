def climbingStairs(n):
    dp = [-1 for i in range(n + 1)]
    return _climbingStairs(n, dp)
def _climbingStairs(n, dp):
    if n <= 2:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = _climbingStairs(n - 1, dp) + _climbingStairs(n - 2, dp)
    return dp[n]

print(climbingStairs(6))