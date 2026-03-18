def bubbleSort(list):
    n = 0
    swap = 0
    while n < len(list) - 1:
        if list[n] > list[n + 1]:
            k = list[n]
            list[n] = list[n + 1]
            list[n + 1] = k
            swap += 1
            n += 1
        else:
            n += 1
    if swap == 0:
        return list
    else:
        return bubbleSort(list)

print(bubbleSort([1,9,6,7]))