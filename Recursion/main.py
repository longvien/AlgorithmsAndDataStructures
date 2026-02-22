# def factorial(x):
#     factorial = 1
#     for i in range (1, x + 1):
#         factorial*= i
#     print(factorial)
#
# factorial(5)

def _factorial(n):
    if n < 2:
        return 1
    return n * _factorial(n - 1) # Solve smaller subproblem
a = _factorial(5)
print(a)


# def sumOfList(list):
#     sum = 0
#     for i in list:
#         sum += i
#     print(sum)
#
# list = [1, 2, 3, 4]
# sumOfList(list)

def _sumOfList(list, i):
    index = i
    if index == len(list):
        return 0
    return list[index] + _sumOfList(list, index + 1) # Solve smaller subproblem
list = [1, 2, 3, 4, 5]
a = _sumOfList(list, 0)
print(a)

