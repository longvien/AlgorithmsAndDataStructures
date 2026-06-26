#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0] == 1) {return 0;}
        int rN = obstacleGrid.size();
        int cN = obstacleGrid[0].size();
        vector<vector<int>> dp(rN, vector<int>(cN, 0));
        dp[0][0] = 1;
        for (int i = 0; i < cN; i++) {
            if (i < cN) {
                if (obstacleGrid[0][i] == 1) { break; }
                dp[0][i] = 1;
            }
        }
        for (int j = 0; j < rN; j++) {
            if (j < rN) {
                if (obstacleGrid[j][0] == 1) { break; }
                dp[j][0] = 1;
            }
        }
        for (int r = 1; r < rN; r++) {
            for (int c = 1; c < cN; c++) {
                if (obstacleGrid[r][c] == 1) {
                    dp[r][c] = 0;
                    continue;
                }
                dp[r][c] = dp[r-1][c] + dp[r][c-1];
            }
        }
        return dp[rN-1][cN-1];
    }
};