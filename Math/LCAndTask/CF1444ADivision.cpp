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


ll fastPow(ll a, ll b) {
    ll ans = 1;
    while (b>0) {
        if (b&1) {
            ans*=a;
        }
        a*=a;
        b>>=1;
    }
    return ans;
}

unordered_map<ll, ll> pF(ll a) {
    unordered_map<ll, ll> ans;
    for (ll i = 2; i <= a/i; i++) {
        if (a==1) {break;}
        if (a%i==0) {
            ll count = 0;
            while (a%i==0) {
                count++;
                a/=i;
            }
            ans[i] = count;
        }
    }
    if (a>1) {ans[a] = 1;}
    return ans;
}

void solve(unordered_map<ll, ll> pM, unordered_map<ll, ll> qM, ll p) {
    ll ans = 0;
    for (auto& [n, e] : pM) {
        if (qM.count(n) != 0) {
            ans = max(ans, p/fastPow(n, pM[n]-qM[n]+1));
        }
    }
    cout << ans << "\n";
}

signed main() {
    FastIO::init();
    ll t;
    cin >> t;
    for (ll i = 0; i<t; i++) {
        ll p, q;
        cin >> p >> q;
        if (p%q != 0) {
            cout << p << "\n";
        }
        else {
            unordered_map<ll, ll> pM = pF(p);
            unordered_map<ll, ll> qM = pF(q);
            solve(pM, qM, p);
        }
    }
    return 0;
}