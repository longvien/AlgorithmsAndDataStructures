#include <bits/stdc++.h>
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

ll modpow(ll n, ll p, ll m) {
    ll ans = 1;
    n%=m;
    while(p>0) {
        if (p&1) {
            ans = ((__int128)ans * n)%m;
        }
        n = ((__int128)n*n)%m;
        p>>=1;
    }
    return ans;
}

signed main() {
    FastIO::init();
    ll n, k, m=MOD;
    cin >> n >> k;
    vector<ll> fact(n+1, 1);
    for (ll i=1;i<n+1;i++) { 
        fact[i] = (fact[i-1]*i%m)%m; 
    }
    cout << (fact[n] * modpow(fact[k]*fact[n-k], m-2, m))%m << "\n";    // C(n,k) mod m = n!/k!(n-k)! mod m = (n!mod m * (k!(n-k)!)^-1 mod m) mod m;
    return 0;
}

// aplies only for 1 query since in this version, we only need to 