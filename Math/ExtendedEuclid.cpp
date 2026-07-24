#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
typedef long long ll;
#define mp make_pair
#define fi first
#define se second

pair<ll, ll> ExtendedEuclidean(ll a, ll b) {
    if (b == 0) {return mp(1, 0);}
    ll q = a/b;
    ll mod = a - q*b;
    ll x1 = 1, y1 = 0;
    ll x2 = 0, y2 = 1;
    ll x3 = 0, y3 = 0;
    while (mod!=0) {
        x3 = x1 - q*x2;
        y3 = y1 - q*y2;
        a = b;
        b = mod;
        x1 = x2;
        y1 = y2;
        x2 = x3;
        y2 = y3;
        q = a/b;
        mod = a-q*b;
    }
    return mp(x2, y2);
}

int main() {
    ll a, b;
    cin >> a >> b;
    pair<ll, ll> ans = ExtendedEuclidean(a, b);
    cout << "x = " << ans.fi << ", y = " << ans.se << "\n";
    return 0; 
}

/*solve Bézout's Identity ( ax + by = gcd(a, b) ) with Extended Euclidean Algorithms. */