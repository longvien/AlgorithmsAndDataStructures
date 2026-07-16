#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> dp(n, vector<int>(m, 0));
        for (int i = 0; i < m; i++) {
            dp[0][i] = grid[0][i];
        }
        for (int r = 1; r < n; r++) {
            for (int c = 0; c < m; c++) {
                int min = 0;
                if (c==0) {
                    min = *min_element(dp[r-1].begin() + 1,  dp[r-1].end());
                }
                else if (c==m-1) {
                    min = *min_element(dp[r-1].begin(), dp[r-1].end() - 1);
                }
                else {
                    int m1 = *min_element(dp[r-1].begin(), dp[r-1].begin() + c);
                    int m2 = *min_element(dp[r-1].begin() + c + 1, dp[r-1].end());
                    min = std::min(m1, m2);
                }
                dp[r][c] = min + grid[r][c];
            }
        }
        return dp[n-1][m-1];
    }
};


int main () {
    Solution mySolu = Solution();
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    cout << mySolu.minFallingPathSum(grid);
}
