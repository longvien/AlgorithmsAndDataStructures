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
    vector<ll> fact(lg+1, 1);
    vector<ll> invfact(lg+1, 1);
    for (ll i=1; i<fact.size(); i++) {
        fact[i] = ((__int128)fact[i-1]*i%MOD)%MOD; 
    }
    invfact[lg] = modpow(fact[lg], MOD-2, MOD);
    for (ll i = lg-1; i>=0; i--) {
        invfact[i] = ((__int128)invfact[i+1]*(i+1))%MOD;
    } 
    for (auto& [n, k] : q) {
        ll ans = ((__int128)((__int128)fact[n]%MOD * invfact[k]%MOD)%MOD * invfact[n-k]%MOD)%MOD; // (a*b*c)modm = ((amodm * bmodm)modm * cmodm) modm 
        cout << "C(" << n << ", " << k << ") = " << ans << "\n"; 
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