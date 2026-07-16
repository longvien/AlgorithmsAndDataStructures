#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word2.size()+1, vector<int>(word1.size()+1, 0));
        for (int r = 0 ; r < word2.size()+1; r++) {
            dp[r][0] = r;
        }
        for (int c = 0; c < word1.size()+1; c++) {
            dp[0][c] = c;
        }
        for (int i = 1; i < word2.size()+1; i++) {
            for (int j = 1; j < word1.size()+1; j++) {
                if (word2[i-1] == word1[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                }
                else {
                    dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                }
            }
        }
        return dp[word2.size()][word1.size()];
    }
};