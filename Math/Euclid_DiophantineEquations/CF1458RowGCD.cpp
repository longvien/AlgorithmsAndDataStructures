#include <bits/stdc++.h>
using namespace std;
using ll = signed long long;
#define f(i,a,n) for (ll i = a; i<n; i++)
#define pb push_back
#pragma GCC optimize("O3")

namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

void solve(vector<ll> a, vector<ll> b) {
    ll a1 = a[0];
    ll ggt = 0;
    ll a2 = 0;
    f(i,1,a.size()) {
        if (ggt==0) {
            ggt = a[i]-a1;
            continue;
        }
        else {
            a2 = a[i]-a1;
            ggt = gcd(ggt, a2);
        }
    }
    f(i,0,b.size()) {
        cout << gcd(a1+b[i], ggt);
        if (i<b.size()-1) {cout << " ";}
    }
}

signed main() {
    FastIO::init();
    ll n, m;
    cin >> n >> m;
    vector<ll> a;
    vector<ll> b;
    f(i,0,n) {
        ll curr;
        cin >> curr;
        a.pb(curr);
    }
    f(i,0,m) {
        ll curr;
        cin >> curr;
        b.pb(curr);
    }
    solve(a, b);
    cout << "\n";
    return 0;
}

