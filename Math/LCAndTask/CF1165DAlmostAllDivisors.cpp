#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#pragma GCC optimize("O3")

namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

bool check(unordered_set<ll> n, ll a) {
    bool ans = true;
    for (ll i = 2; i <= a/i; i++) {
        if (a%i == 0) {
            if (n.find(i)==0 || n.find(a/i)==0) {
                ans = false;
                break;
            }
        }
    }
    return ans;
}

ll solve(vector<ll> n) {
    sort(n.begin(), n.end()); // O(nlogn)
    ll s = n.size();
    ll ans = 1;
    for (ll i = 0; i <= floor(s/2); i++) {
        if (i==0) { ans = n[0]*n[s-1]; }
        else {
            ll curr = n[i]*n[s-1-i];
            if (curr!=ans) {
                ans = -1;
                break;
            }
            else {
                continue;
            }
        }
    }
    return ans;
}

signed main() {
    FastIO::init();
    ll t;
    cin >> t;
    for (ll i = 0; i<t; i++) {
        ll l;
        cin >> l;
        vector<ll> nums;
        unordered_set<ll> nS;
        for (ll j = 0; j < l; j++) {
            ll curr;
            cin >> curr;
            nums.push_back(curr);
            nS.insert(curr);
        }
        ll ans = solve(nums);
        if (ans == -1) {
            cout << ans << "\n";
            continue;
        }
        cout << (check(nS, ans)? ans : -1) << "\n";
    }
    return 0;
}