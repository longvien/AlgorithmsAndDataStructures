#memoization
def HouseRobberM(houses):
    if len(houses) == 1:
        return houses[0]
    dp = [-1 for i in range(len(houses))]
    dp[0] = houses[0]
    dp[1] = max(dp[0], houses[1])
    return _HouseRobberM(houses, dp, len(houses) - 1)

def _HouseRobberM(house, dp, n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = max(_HouseRobberM(house, dp, n - 1), _HouseRobberM(house, dp, n - 2) + house[n])
    return dp[n]

houses = [2,7,9,3,1]
print(HouseRobberM(houses))
#tabulation
def HouseRobberT(houses):
    if len(houses) == 1:
        return houses[0]
    dp = [-1 for i in range(len(houses))]
    dp[0] = houses[0]
    dp[1] = max(dp[0], houses[1])
    if len(houses) == 2:
        return dp[1]
    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
    return dp[len(houses) - 1]

print(HouseRobberT([2,7,9,3,1]))