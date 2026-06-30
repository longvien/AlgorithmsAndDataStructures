#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix[0].size();
        int n = matrix.size();
        vector<vector<int>> dp(n, vector<int>(m, 0));
        for (int i = 0; i < m; i++) {
            dp[0][i] = matrix[0][i];
        }
        for (int r = 1; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (c==0) {
                    dp[r][c] = min({dp[r - 1][c+1], dp[r - 1][c]}) + matrix[r][c];
                }
                else if (c==n-1) {
                    dp[r][c] = min({dp[r - 1][c-1], dp[r - 1][c]}) + matrix[r][c];
                }
                else {
                    dp[r][c] = min({dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]}) + matrix[r][c];
                }
            }
        }
        return *min_element(dp[n-1].begin(), dp[n-1].end());
    }
};

int main() {
    Solution mySolu = Solution();
    vector<vector<int>> matrix = {{2,1,3},{6,5,4},{7,8,9}};
    cout << mySolu.minFallingPathSum(matrix);
}

