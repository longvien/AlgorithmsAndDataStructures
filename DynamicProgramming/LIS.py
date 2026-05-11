# #LIS | Largest Increasing Subsequence
#tabulation
def LIST(nums):
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        for n in range(i - 1, -1, -1):
            if nums[n] < nums[i]:
                dp[i] = max(dp[i], dp[n] + 1)
    print(dp)
    maxL = max(dp)
    return maxL
arr = [1, 2, 5, 6, 7, 5, 4, 4]
print(LIST(arr)) # Pass! Time Complexity: 0(n**2)