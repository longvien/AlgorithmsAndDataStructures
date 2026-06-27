#include <utility>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int nr = board.size();
        int nc = board[0].size();
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {1, 1}};
        vector<vector<pair<int, int>>> dp(nr, vector<pair<int, int>>(nc, {0, 0}));
        dp[nr-1][nc-1] = {0, 1};
        for (int r = nr-2; r > -1; r--) {
            if (r > -1) {
                if (board[r][nc-1] != 'X') {
                    dp[r][nc-1] = {dp[r+1][nc-1].first + board[r][nc-1] - '0', 1};
                } 
                else {break;}
            }
        }
        for (int c = nc-2; c > -1; c--) {
            if (c > -1) {
                if (board[nr-1][c] != 'X') {
                    dp[nr-1][c] = {dp[nr-1][c+1].first + board[nr-1][c] - '0', 1};
                }
                else {break;}
            }
        }
        for (int r = nr-2; r > -1; r--) {
            for (int c = nc-2; c > -1; c--) {
                if (board[r][c] == 'X') {continue;}
                else {
                    char currC = board[r][c];
                    int curr = currC - '0';
                    if (r == 0 && c == 0) {
                        curr = 0;
                    }
                    for (const auto&[dr, dc] : directions) {
                        int oR = r + dr;
                        int oC = c + dc;
                        if (board[oR][oC] != 'X' && dp[oR][oC].second != 0) {
                            if (dp[r][c].first < curr + dp[oR][oC].first) {
                                dp[r][c] = {curr + dp[oR][oC].first, dp[oR][oC].second};
                            }
                            else if (dp[r][c].first == curr + dp[oR][oC].first) {
                                int ways = (dp[r][c].second + dp[oR][oC].second) % 1000000007;
                                dp[r][c] = {dp[r][c].first, ways};
                            }
                        }
                    }
                }
            }
        }
        return {dp[0][0].first, dp[0][0].second};
    }
};


int main() {
    Solution mySolu = Solution();
    vector<string> in = {"EX","XS"};
    vector<int> ans = mySolu.pathsWithMaxScore(in);

    for (auto& c : ans) {
        cout << c << " ";
    }
}
