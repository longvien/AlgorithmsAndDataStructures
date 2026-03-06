def sumOfList(list):
    return _sumOfList(list, 0)
def _sumOfList(list, index):
    if index == len(list) - 1:
        return list[index]
    return list[index] + _sumOfList(list, index + 1)

list = [1, 2, 3, 4, 5]
print(sumOfList(list))