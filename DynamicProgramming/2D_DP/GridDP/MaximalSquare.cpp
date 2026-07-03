#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int maxSqr = 0;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>>dp(m, vector<int>(n, 0));
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r == 0 || c == 0) {
                    if (matrix[r][c] == '1') {
                        dp[r][c] = 1;
                        maxSqr = max(maxSqr, dp[r][c]);
                    }
                }
                else if (matrix[r][c] == '1' && matrix[r-1][c-1] == '1') {
                    dp[r][c] = dp[r-1][c-1] + 1;
                    maxSqr = max(maxSqr, dp[r][c]);
                }
            }
        }
        return maxSqr;
    }
};

int main() {
    Solution mySolu = Solution();
    vector<vector<char>> n = {
    {'1', '0', '1', '0', '0'},
    {'1', '0', '1', '1', '1'},
    {'1', '1', '1', '1', '1'},
    {'1', '0', '0', '1', '0'}
};
    cout << mySolu.maximalSquare(n);
}