#memoization
def fib(n):
    memo = [-1 for i in range(n + 1)]
    return _fib(n, memo)
def _fib(n, memo):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]

#tabulation
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

print(fibo(6))