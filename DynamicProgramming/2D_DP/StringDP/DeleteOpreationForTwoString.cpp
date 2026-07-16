#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        vector<vector<int>> dp(n, vector<int>(m, 0));
        if (word1[0] == word2[0]) {
            dp[0][0] = 1;
        }
        for (int i = 1; i < n; i++) {
            dp[i][0] = (word1[i] == word2[0])? 1 : dp[i-1][0];
        }
        for (int i = 1; i < m; i++) {
            dp[0][i] = (word1[0] == word2[i])? 1 : dp[0][i-1];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                dp[i][j] = (word1[i] == word2[j])? dp[i-1][j-1] + 1 : max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return (n+m) - dp[n-1][m-1]*2;
    }
};