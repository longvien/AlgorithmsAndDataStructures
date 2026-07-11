#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n=dungeon.size();
        int m=dungeon[0].size();
        vector<vector<int>> dp(n, vector<int>(m, 0));
        int ans=0-dungeon[n-1][m-1]+1;
        dp[n-1][m-1]=(ans<1)?1:ans;
        for (int i=n-2; i>-1; i--) {
            ans=dp[i+1][m-1]-dungeon[i][m-1];
            dp[i][m-1]=(ans<1)?1:ans;  
        }   
        for (int i=m-2; i>-1; i--) {
            ans=dp[n-1][i+1]-dungeon[n-1][i];
            dp[n-1][i]=(ans<1)?1:ans;
        }
        for (int r=n-2; r>-1; r--) {
            for (int c=m-2; c>-1; c--) {
                ans=min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c];
                dp[r][c]=(ans<1)?1:ans; 
            }
        }
        return dp[0][0];
    }
};