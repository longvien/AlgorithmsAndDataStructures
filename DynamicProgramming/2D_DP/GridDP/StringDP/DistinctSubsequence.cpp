#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
#pragma GCC optimize("O3")

class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size();
        int m = t.size();
        if (n < m) {return 0;}
        vector<vector<ull>> dp(n, vector<ull>(m, 0));
        if (s[0] == t[0]) {
            dp[0][0] = 1;
        }
        for (int i = 1; i < n; i++) {
            dp[i][0] = (s[i] == t[0])? dp[i-1][0]+1 : dp[i-1][0];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                dp[i][j] = (s[i] == t[j])? dp[i-1][j-1] + dp[i-1][j] : dp[i-1][j];
            }
        }
        return dp[n-1][m-1];
    }
};