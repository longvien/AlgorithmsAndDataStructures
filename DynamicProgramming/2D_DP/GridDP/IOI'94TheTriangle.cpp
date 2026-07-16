#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")

int solve(vector<vector<int>>& grid, vector<vector<int>>& dp) {
    dp[0][0] = grid[0][0];
    for (int i = 1; i < dp.size(); i++) {
        dp[i][0] = dp[i-1][0]+grid[i][0];
        dp[i][i] = dp[i-1][i-1]+grid[i][i];
    }
    for (int i = 2; i < dp.size(); i++) {
        for (int j = 1; j < i; j++) {
            dp[i][j] = max({dp[i-1][j-1], dp[i-1][j]}) + grid[i][j];
        }
    }
    return *max_element(dp[dp.size()-1].begin(), dp[dp.size()-1].end());
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    vector<vector<int>> grid;
    vector<vector<int>> dp;
    for (int i = 0; i < t; i++) {
        vector<int> curr;
        for (int j = 0; j < i+1; j++) {
            int num;
            cin >> num;
            curr.push_back(num);
        }
        grid.push_back(curr);
        dp.push_back(vector<int>(i+1, 0));
    }
    cout << solve(grid, dp);
    return 0;
}