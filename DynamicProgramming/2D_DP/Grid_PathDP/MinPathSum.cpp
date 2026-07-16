#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), 0));
        int rS = grid.size();
        int cS = grid[0].size();
        dp[0][0] = grid[0][0];
        for (int c = 1; c < cS; c++) {
            dp[0][c] = dp[0][c-1] + grid[0][c];
        }
        for (int r = 1; r < rS; r++) {
            dp[r][0] = dp[r-1][0] + grid[r][0];
        }

        for (int rows = 1; rows < rS; rows++) {
            for (int cols = 1; cols < cS; cols++) {
                dp[rows][cols] = min(dp[rows-1][cols], dp[rows][cols-1]) + grid[rows][cols];
            }
        }
        return dp[rS -1][cS -1];
    }
};