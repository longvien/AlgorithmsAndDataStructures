#include <bits/stdc++.h>
using namespace std;
using ll = signed long long;
#define pb push_back
#pragma GCC optmize("O3")

namespace FastIO {
	inline void init() {
		ios_base::sync_with_stdio(false);
		cin.tie(nullptr);
	}
}
// c(n, k) = c(n-1, k-1) + c(n-1, k)
ll solve(ll n, ll k) { 
    vector<vector<ll>> dp;
    ll ans = 0;
    for (ll i = 0; i<n+1; i++) {
        dp.pb(vector<ll>(i+1, 0));
    }
    dp[0][0] = 1;
    for (ll i = 1; i<dp.size(); i++) {
        for (ll j = 0; j<dp[i].size(); j++) {
            dp[i][j] = (j == 0 || j == dp[i].size()-1)? 1 : dp[i-1][j-1] + dp[i-1][j];
            if (i==n && j==k) {
                ans = dp[i][j];
                break;
            }
        }
        if (ans!=0) {break;}
    }
    return ans;
}

signed main() {
    FastIO::init();
    ll n, k;
    cin >> n >> k;
    if (n<k) {
        cout << 0 << "\n";
        return 0;
    }
    else if (n==k) { 
        cout << 1 << "\n";
        return 0; 
    }
    cout << solve(n, k) << "\n"; 
    return 0;
}
// Time Complexity: O(n^2)