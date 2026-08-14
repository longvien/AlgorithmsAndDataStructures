#include<bits/stdc++.h>
using namespace std;
using ll = signed long long;
#pragma GCC optimize("O3")

namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

ll MOD = 1e9+7;

ll modpow(ll a, ll b, ll m) {
    ll ans = 1;
    a%=m;
    while (b>0) {
        if (b&1) {
            ans = ((__int128)ans * a)%m;
        }
        a = ((__int128)a*a)%m;
        b>>=1;
    }
    return ans;
}

void solve(vector<pair<ll, ll>> q, ll lg) {
    vector<ll> fact(lg+1, 0);
    vector<ll> invfact(lg+1, 0);
    for (ll i=1; i< q.size(); i++) {
        fact[i] = (fact[i-1]*i%MOD)%MOD;
    }
    invfact[lg] = modpow(lg, MOD-2, MOD);
    for (ll i = lg-1; i>=0; i--) {
        invfact[i] = (invfact[i+1]*i+1%MOD)%MOD;
    } 
    for (auto& [n, k] : q) {
        cout << "C(" << n << ", " << k << ") = " << fact[n] * invfact[k] * invfact[n-k] << "\n"; 
    }
}

signed main() {
    FastIO::init();
    ll t;
    cin >> t;
    ll lg = 0;
    vector<pair<ll, ll>> q;
    for (ll i=0; i<t; i++) {
        ll n, k;
        cin >> n >> k;
        lg = max(lg, n);
        q.push_back({n, k}); 
    }
    solve(q, lg);
    return 0;    
}