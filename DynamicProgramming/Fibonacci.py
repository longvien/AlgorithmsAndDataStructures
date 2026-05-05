#memoization
def fiboM(x):
    dp = [-1 for i in range(x + 1)]
    return _fiboM(x ,dp)
def _fiboM(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = _fiboM(n - 1, dp) + _fiboM(n - 2, dp)
    return dp[n]

print(fiboM(6))

#tabulation:

def fiboT(x):
    dp = [-1 for i in range(x+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, x+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[x]
print(fiboT(7))
