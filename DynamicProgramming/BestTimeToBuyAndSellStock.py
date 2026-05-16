def maxProfit(prices: list[int]) -> int:
    maxPr = 0
    minN = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > minN:
            maxPr = max(maxPr, prices[i] - minN)
        else:
            minN = prices[i]
    return maxPr
print(maxProfit([7,1,5,3,6,4]))