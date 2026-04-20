#memoization
def fib(n):
    dp = [-1 for i in range(n + 1)]
    return _fib(n, dp)
def _fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = _fib(n - 1, dp) + _fib(n - 2, dp)
    return dp[n]

#tabulation
def fibonacci(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

#tabulation | Optimized
def fibo(n):
    n1 = 0
    n2 = 1
    if n <= 1:
        return n
    for i in range(n - 1):
        current = n2
        n2 = n1 + n2
        n1 = current
    return n2

print(fib(6)) # 8
print(fibo(6)) # 8
print(fibonacci(6)) # 8