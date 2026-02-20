def factorial(x):
    factorial = 1
    for i in range (1, x + 1):
        factorial*= i
    print(factorial)

factorial(5)

def _factorial(n):
    if n < 2:
        return 1
    return n * _factorial(n - 1)

a = _factorial(5)
print(a)
