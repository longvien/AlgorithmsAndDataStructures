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

ll solve() {

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
 
    return 0;
}

