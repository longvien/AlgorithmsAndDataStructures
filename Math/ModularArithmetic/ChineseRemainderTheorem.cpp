#include <bits/stdc++.h>
using namespace std;
using ll = signed long long;
#define mp make_pair
#define pb push_back
template<typename T>
using vpair = vector<pair<T, T>>;
#pragma GCC optimize("O3")

namespace FastIO {
	inline void init() {
		ios_base::sync_with_stdio(false);
		cin.tie(nullptr);
	}
}

ll extendedEuclid(ll a, ll b, ll m) {
    ll x1 = 1, x2 = 0, x3 = 0;
    ll y1 = 0, y2 = 1, y3 = 0;
    ll q = a/b;
    ll r = a%b;
    while (b!=1) {
        a = b;
        b = r;
        x3 = x1 - q*x2;
        y3 = y1 - q*y2;
        x1 = x2;
        x2 = x3;
        y1 = y2;
        y2 = y3;
        q = a/b;
        r = a%b;
    }
    return (x2%m+m)%m;
}

ll CRT(vpair<ll> in, ll M) {
    ll ans = 0; // x = k ∑ i=1 aiMi((x^-1)mod mi)
    for (auto& [r, m] : in) {
        ll currX = M/m;
        currX = ((__int128)currX*(r%M))%M;
        currX = ((__int128)currX*(extendedEuclid(M/m, m, m))%M)%M;
        ans = (ans+currX)%M;
    }
    return ans;
}

signed main() {
    FastIO::init();
    ll t;
    cin >> t;
    ll productM = 1;    
    vpair<ll> equations;
    for (ll i = 0; i<t; i++) {
        ll r, m;
        cin >> r >> m;
        if (gcd(productM, m) != 1) {
            cout << "This is the standard crt algorithm, moduli must be co prime to each other!" << "\n";
            return 0;
        }
        equations.pb({r, m});
        productM*=m;
    }
    cout << "Smallest value of x which sastify the equations is: " << CRT(equations, productM) << "\n";
    return 0;
}