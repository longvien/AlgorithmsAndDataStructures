#include <bits/stdc++.h>
using namespace std;
using ll = signed long long;
#define f(i,a,n) for (ll i = a; i<n; i++)
#define pb push_back
//#pragma GCC optimize("O3")

namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

signed main() {
    FastIO::init();
    ll n, m;
    cin >> n >> m;
    ll a1;
    ll ggt = 0;
    ll a2;
    vector<ll> b;
    f(i,0,n) {
        if (i==0) {cin >> a1;}
        cin >> a2;
        ggt = gcd(a2-a1, ggt);
    }
    f(i,0,m) {
        ll curr;
        cin >> curr;
        b.pb(curr);
    }
    f(i,0,m) {
        cout << gcd(a1+b[i], ggt);
        if (i<m-1) {cout << " ";}
    }
    return 0;
}

