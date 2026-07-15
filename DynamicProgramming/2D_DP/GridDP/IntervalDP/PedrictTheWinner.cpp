#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#pragma GCC optimize("O3")

class Solution {
public:
    bool predictTheWinner(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) { return true;}
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i<n-1; i++) {
            dp[i][i] = nums[i];
            dp[i][i+1] = max({nums[i], nums[i+1]});
        }
        dp[n-1][n-1] = nums[n-1];

        for (int i = n-3; i>-1; i--){
            for (int j = i+2; j<n; j++) {
                dp[i][j] = max({min({dp[i+2][j], dp[i+1][j-1]})+nums[i], min({dp[i+1][j-1], dp[i][j-2]})+nums[j]});
            }
        }
        ll sum = accumulate(nums.begin(), nums.end(), 0);
        return dp[0][n-1] >= sum - dp[0][n-1]; 
    }
};
