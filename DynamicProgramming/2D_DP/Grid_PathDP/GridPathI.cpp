#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#pragma GCC optimize("O3")

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll mod = 1e9 + 7;
    int t;
    cin >> t;
    vector<vector<char>> grid;
    for (int i = 0; i < t; i++) {
        vector<char> c;
        for (int k = 0; k < t; k++) {
            char n;
            cin >> n;
            c.push_back(n);
        }
        grid.push_back(c);
    }
    if (grid[0][0] == '*') {cout << 0;}
    else {
        vector<vector<int>> dp(grid.size(), vector<int>(grid.size(), 1%mod));
        for (int i = 1; i < grid.size(); i++) {
            dp[0][i] = (dp[0][i-1] == 1 && grid[0][i] == '.')? 1%mod : 0%mod;
            dp[i][0] = (dp[i-1][0] == 1 && grid[i][0] == '.')? 1%mod : 0%mod;
        }
        for (int i = 1; i < grid.size() ; i++) {
            for (int j = 1; j < grid.size(); j++) {
                dp[i][j] = (grid[i][j] == '.')? (dp[i][j-1] + dp[i-1][j])%mod : 0%mod;
            }
        }
        cout << dp[grid.size()-1][grid.size()-1];
    }
}