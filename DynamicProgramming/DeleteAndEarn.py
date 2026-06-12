class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        napr = {}
        for n in nums:
            if n not in napr:
                napr[n] = 0
            napr[n] += n
        rob = []
        for i in napr:
            rob.append((i, napr[i]))
        rob.sort(key=self.getKey)
        dp = [0 for i in range(len(rob))]
        dp[0] = rob[0][1]
        if len(dp) == 1: return dp[0]
        if abs(rob[1][0] - rob[0][0]) > 1:
            dp[1] = dp[0] + rob[1][1]
        else:
            dp[1] = max(rob[0][1], rob[1][1])
        for i in range(2, len(rob)):
            if abs(rob[i][0] - rob[i - 1][0]) > 1:
                dp[i] = dp[i - 1] + rob[i][1]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + rob[i][1])
        return dp[len(dp) - 1]
    def getKey(self, n):
        return n[0]
