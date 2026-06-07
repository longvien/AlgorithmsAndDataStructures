class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0' or s[0] == '0': return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '0' or int(s[i - 1] + '0') > 26:
                    return 0
                if i == 1:
                    dp[i + 1] = dp[i]
                else:
                    dp[i + 1] = dp[i - 1]
            elif s[i - 1] == '0':
                dp[i + 1] = dp[i]
            else:
                if int(s[i-1] + s[i]) > 26:
                    dp[i + 1] = dp[i]
                else:
                    dp[i + 1] = dp[i] + dp[i - 1]
        return dp[len(s)]