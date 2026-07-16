#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int nr = triangle.size();
        vector<vector<int>> dp;
        for (int i = 0; i < nr; i++) {
            dp.push_back(vector<int>(i+1, 0));
        }
        dp[0][0] = triangle[0][0];
        for (int r = 1; r < nr; r++) {
            for (int c = 0 ; c < r+1; c++) {
                if (c==0) {
                    dp[r][c] = dp[r-1][c] + triangle[r][c];
                }
                else if (c==r) {
                    dp[r][c] = dp[r-1][c-1] + triangle[r][c];
                }
                else {
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c-1]) + triangle[r][c];
                }
            }
        }
        auto ans = min_element(dp[nr-1].begin(), dp[nr-1].end());
        return *ans;
    }
};