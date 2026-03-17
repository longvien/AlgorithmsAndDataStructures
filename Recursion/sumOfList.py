def sumOfList(list):
    return _sumOfList(list, 0)
def _sumOfList(list, index):
    if index == len(list):
        return 0
    return list[index] + _sumOfList(list, index + 1)

myList = [110, 3, 4]
print(sumOfList(myList))