#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;

namespace FastIO {
    inline void init() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
    }
};

signed main() {
    FastIO::init();
    int n, v;
    cin >> n >> v;
    vector<int> IN, dp(v+1, 0);
    dp[0] = 1;
    for (int i = 0; i < n; i++) {
        int curr;
        cin >> curr;
        IN.push_back(curr);
    }
    for (int i = 0; i < IN.size(); i++) {
        for (int j = v; j >= 1; j--) {
            if (IN[i] <= j) dp[j] |= dp[j-IN[i]];
        }
    }
    cout << dp[v] << "\n";
    return 0;
}


